#!/usr/bin/env python3
"""
Script local de suivi/envoi pour le fichier influenceurs-hce-suivi.html.
A LANCER TOI-MEME (jamais par une automatisation) : c'est volontaire, l'envoi
d'emails reste un geste humain.

Usage :
  python3 hce_outreach.py send
      Envoie tous les emails prets (badge exactement "A valider" + adresse
      email presente), met a jour les statuts automatiquement.

  python3 hce_outreach.py mark-dm "@handle"
      A lancer juste apres avoir envoye un DM toi-meme depuis l'app.
      Marque la carte comme "Contacte" (count+1, date du jour).

  python3 hce_outreach.py mark-status "@handle" repondu|accepte|refuse
      Marque une reponse recue. Ces statuts ne sont plus jamais touches
      par la routine automatique (elle ne relance jamais quelqu'un qui a
      repondu, accepte ou refuse).

  python3 hce_outreach.py list
      Affiche l'etat actuel de toutes les cartes (rien n'est modifie).

  python3 hce_outreach.py list-folders
      Liste les vrais noms de dossiers IMAP du compte (diagnostic, en cas
      de souci pour retrouver les emails envoyes dans le dossier Envoyes).

Le mot de passe est demande a chaque lancement (getpass, jamais stocke,
jamais dans l'historique du terminal).
"""
import sys
import re
import ssl
import ast
import smtplib
import imaplib
import getpass
import datetime
import html
from email.mime.text import MIMEText
from email.header import Header
from pathlib import Path

TRACK_FILE = Path(__file__).resolve().parent / "influenceurs-hce-suivi.html"
SENDER = "contact@harnais-chien-expert.fr"
SMTP_HOST, SMTP_PORT = "smtp.hostinger.com", 465
IMAP_HOST, IMAP_PORT = "imap.hostinger.com", 993

CARD_RE = re.compile(r"<!-- CARD (.*?) -->\n(.*?)<!-- /CARD -->", re.S)
ATTR_RE = re.compile(r'(\w[\w-]*)="((?:[^"\\]|\\.)*)"')
BADGE_RE = re.compile(r'<span class="badge [\w-]+">[^<]*</span>')
NOTES_RE = re.compile(r'(<div class="notes">)(.*?)(</div>)', re.S)


def parse_attrs(attr_str):
    return {m.group(1): m.group(2) for m in ATTR_RE.finditer(attr_str)}


def build_marker(attrs):
    parts = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    return f"<!-- CARD {parts} -->"


def load():
    return TRACK_FILE.read_text(encoding="utf-8")


def save(text):
    TRACK_FILE.write_text(text, encoding="utf-8")


def get_cards(text):
    """Returns list of dicts: attrs, body, full_match (re.Match)."""
    cards = []
    for m in CARD_RE.finditer(text):
        attrs = parse_attrs(m.group(1))
        cards.append({"attrs": attrs, "body": m.group(2), "match": m})
    return cards


def set_badge(body, css_class, label):
    return BADGE_RE.sub(f'<span class="badge {css_class}">{label}</span>', body, count=1)


def append_note(body, text):
    return NOTES_RE.sub(lambda m: m.group(1) + m.group(2) + f" — {text}" + m.group(3), body, count=1)


def get_draft_body(body):
    m = re.search(r'<div class="draft-body">(.*?)</div>', body, re.S)
    return html.unescape(m.group(1)).strip() if m else None


def apply_updates(text, updates):
    """updates: dict handle -> (new_attrs, new_body). Rewrites the file once."""
    def repl(m):
        attrs = parse_attrs(m.group(1))
        handle = attrs.get("handle")
        if handle in updates:
            new_attrs, new_body = updates[handle]
            return build_marker(new_attrs) + "\n" + new_body + "<!-- /CARD -->"
        return m.group(0)
    return CARD_RE.sub(repl, text)


def send_mail(smtp, to_addr, subject, body):
    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = Header(subject, "utf-8")
    msg["From"] = SENDER
    msg["To"] = to_addr
    msg["Date"] = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S %z")
    raw = msg.as_bytes()
    smtp.sendmail(SENDER, [to_addr], raw)
    return raw


SENT_FOLDER_CANDIDATES = ["Sent", "INBOX.Sent", "Sent Items", "INBOX.Sent Items", "INBOX/Sent"]


def append_to_sent(password, raw_message):
    try:
        imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        imap.login(SENDER, password)
    except Exception as ex:
        print(f"  (avertissement : connexion IMAP impossible, pas de copie dans Envoyes : {ex})", file=sys.stderr)
        return
    ok = False
    for folder in SENT_FOLDER_CANDIDATES:
        try:
            typ, _ = imap.append(folder, "", imaplib.Time2Internaldate(datetime.datetime.now().timestamp()), raw_message)
            if typ == "OK":
                ok = True
                break
        except Exception:
            continue
    imap.logout()
    if not ok:
        print(f"  (avertissement : aucun dossier Envoyes reconnu parmi {SENT_FOLDER_CANDIDATES} — lance 'python3 hce_outreach.py list-folders' pour voir les vrais noms)", file=sys.stderr)


def cmd_list_folders():
    password = getpass.getpass(f"Mot de passe pour {SENDER} : ")
    try:
        imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        imap.login(SENDER, password)
        typ, folders = imap.list()
        imap.logout()
        if typ != "OK":
            print("Impossible de lister les dossiers.")
            return
        print("Dossiers IMAP disponibles :")
        for f in folders:
            print(" ", f.decode(errors="replace"))
    except Exception as ex:
        print(f"Connexion IMAP impossible : {ex}", file=sys.stderr)


def cmd_send():
    text = load()
    cards = get_cards(text)
    todo = []
    for c in cards:
        attrs = c["attrs"]
        badge_m = re.search(r'<span class="badge [\w-]+">([^<]*)</span>', c["body"])
        badge_label = badge_m.group(1) if badge_m else ""
        if attrs.get("contact") == "email" and attrs.get("address") and badge_label == "À valider":
            draft = get_draft_body(c["body"])
            if draft:
                todo.append((attrs, c["body"], draft))

    if not todo:
        print("Rien a envoyer : aucun candidat avec badge \"A valider\" + email.")
        return

    print(f"{len(todo)} email(s) pret(s) a partir :")
    for attrs, _, _ in todo:
        print(f"  - {attrs['handle']} -> {attrs['address']}")
    if input("Confirmer l'envoi ? (o/n) ").strip().lower() != "o":
        print("Annule.")
        return

    password = getpass.getpass(f"Mot de passe pour {SENDER} : ")
    today = datetime.date.today().isoformat()
    updates = {}
    sent_raw = []

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context, timeout=20) as smtp:
            smtp.login(SENDER, password)
            for attrs, body, draft in todo:
                subject = html.unescape(attrs.get("subject") or "Collaboration Harnais Chien Expert")
                try:
                    raw = send_mail(smtp, attrs["address"], subject, draft)
                    sent_raw.append(raw)
                    new_attrs = dict(attrs)
                    new_attrs["count"] = str(int(attrs.get("count", "0")) + 1)
                    new_attrs["last-sent"] = today
                    new_body = set_badge(body, "badge-contacte", "Contacté")
                    new_body = append_note(new_body, f"Contacté le {today}")
                    updates[attrs["handle"]] = (new_attrs, new_body)
                    print(f"  OK  {attrs['handle']}")
                except Exception as ex:
                    print(f"  ECHEC {attrs['handle']} : {ex}")
    except Exception as ex:
        print(f"Connexion SMTP impossible : {ex}", file=sys.stderr)
        sys.exit(1)

    if updates:
        save(apply_updates(text, updates))
        print(f"{len(updates)} carte(s) mise(s) a jour dans le fichier de suivi.")
        for raw in sent_raw:
            append_to_sent(password, raw)


def cmd_mark_dm(handle):
    text = load()
    cards = get_cards(text)
    target = next((c for c in cards if c["attrs"].get("handle") == handle), None)
    if not target:
        print(f"Handle introuvable : {handle}")
        return
    if target["attrs"].get("contact") != "dm":
        print(f"Attention : {handle} n'est pas marque comme contact DM (contact={target['attrs'].get('contact')}). Continue quand meme.")
    today = datetime.date.today().isoformat()
    attrs = dict(target["attrs"])
    attrs["count"] = str(int(attrs.get("count", "0")) + 1)
    attrs["last-sent"] = today
    body = set_badge(target["body"], "badge-contacte", "Contacté")
    body = append_note(body, f"DM envoyé le {today}")
    save(apply_updates(text, {handle: (attrs, body)}))
    print(f"{handle} marque comme Contacte ({today}).")


def cmd_mark_status(handle, status):
    mapping = {
        "repondu": ("badge-repondu", "Répondu"),
        "accepte": ("badge-accepte", "Accepté"),
        "refuse": ("badge-refuse", "Refusé"),
        "sans-reponse": ("badge-sans-reponse", "Sans réponse"),
    }
    if status not in mapping:
        print(f"Statut inconnu : {status}. Choix possibles : {', '.join(mapping)}")
        return
    text = load()
    cards = get_cards(text)
    target = next((c for c in cards if c["attrs"].get("handle") == handle), None)
    if not target:
        print(f"Handle introuvable : {handle}")
        return
    css_class, label = mapping[status]
    body = set_badge(target["body"], css_class, label)
    save(apply_updates(text, {handle: (dict(target["attrs"]), body)}))
    print(f"{handle} -> {label}")


def cmd_list():
    text = load()
    for c in get_cards(text):
        badge_m = re.search(r'<span class="badge [\w-]+">([^<]*)</span>', c["body"])
        badge = badge_m.group(1) if badge_m else "?"
        a = c["attrs"]
        print(f"{a.get('handle', '?'):28} {a.get('contact', '?'):6} {badge:20} envoyes={a.get('count', '0')} dernier={a.get('last-sent') or '-'}")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == "send":
        cmd_send()
    elif cmd == "mark-dm" and len(sys.argv) == 3:
        cmd_mark_dm(sys.argv[2])
    elif cmd == "mark-status" and len(sys.argv) == 4:
        cmd_mark_status(sys.argv[2], sys.argv[3])
    elif cmd == "list":
        cmd_list()
    elif cmd == "list-folders":
        cmd_list_folders()
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
