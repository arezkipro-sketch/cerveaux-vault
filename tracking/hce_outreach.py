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

  python3 hce_outreach.py check-inbox
      Lecture seule (ne marque rien comme lu, n'envoie rien). Liste les
      emails recus depuis 14 jours et signale ceux dont l'expediteur
      correspond a un email connu du fichier de suivi. Sert juste a
      reperer une reponse, la mise a jour du statut reste manuelle
      (mark-status) une fois que tu as lu le contenu.

  python3 hce_outreach.py read "@handle"
      Affiche le texte complet du dernier email recu de ce candidat
      (lecture seule). Pratique pour coller le contenu ici a Claude.

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
from email.header import Header, decode_header
import email as email_lib
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


def cmd_check_inbox():
    text = load()
    cards = get_cards(text)
    known = {
        c["attrs"]["address"].strip().lower(): c["attrs"].get("handle", "?")
        for c in cards
        if c["attrs"].get("address")
    }
    password = getpass.getpass(f"Mot de passe pour {SENDER} : ")
    try:
        imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        imap.login(SENDER, password)
        imap.select("INBOX", readonly=True)
        since_date = (datetime.date.today() - datetime.timedelta(days=14)).strftime("%d-%b-%Y")
        typ, data = imap.search(None, f"(SINCE {since_date})")
        if typ != "OK":
            print("Recherche impossible.")
            imap.logout()
            return
        ids = data[0].split()
        if not ids:
            print(f"Aucun email recu depuis {since_date}.")
            imap.logout()
            return
        print(f"{len(ids)} email(s) recus depuis {since_date} (plus recent en premier) :\n")
        for eid in reversed(ids):
            typ, msg_data = imap.fetch(eid, "(BODY.PEEK[HEADER.FIELDS (FROM SUBJECT DATE)])")
            if typ != "OK" or not msg_data or not msg_data[0]:
                continue
            header = msg_data[0][1].decode(errors="replace")
            from_m = re.search(r"From:\s*(.*)", header)
            subj_m = re.search(r"Subject:\s*(.*)", header)
            date_m = re.search(r"Date:\s*(.*)", header)
            from_addr = (from_m.group(1).strip() if from_m else "?")
            subject = (subj_m.group(1).strip() if subj_m else "?")
            date = (date_m.group(1).strip() if date_m else "?")
            match_handle = next((h for addr, h in known.items() if addr in from_addr.lower()), None)
            tag = f"   <-- reponse possible de {match_handle}" if match_handle else ""
            print(f"[{date}] {from_addr} — {subject}{tag}")
        imap.logout()
        print("\nRien n'a ete marque comme lu. Une fois que tu as identifie une reponse, lis-la dans ta boite puis :")
        print('  python3 hce_outreach.py mark-status "@handle" repondu|accepte|refuse')
    except Exception as ex:
        print(f"Connexion IMAP impossible : {ex}", file=sys.stderr)


def decode_mime_header(value):
    if not value:
        return ""
    parts = decode_header(value)
    out = []
    for text, enc in parts:
        if isinstance(text, bytes):
            out.append(text.decode(enc or "utf-8", errors="replace"))
        else:
            out.append(text)
    return "".join(out)


def extract_plain_text(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain" and "attachment" not in str(part.get("Content-Disposition", "")):
                charset = part.get_content_charset() or "utf-8"
                return part.get_payload(decode=True).decode(charset, errors="replace")
        for part in msg.walk():
            if part.get_content_type() == "text/html" and "attachment" not in str(part.get("Content-Disposition", "")):
                charset = part.get_content_charset() or "utf-8"
                raw = part.get_payload(decode=True).decode(charset, errors="replace")
                return re.sub(r"<[^>]+>", " ", raw)
        return "(pas de contenu texte trouve dans ce message)"
    else:
        charset = msg.get_content_charset() or "utf-8"
        payload = msg.get_payload(decode=True)
        return payload.decode(charset, errors="replace") if payload else msg.get_payload()


def cmd_read(handle):
    text = load()
    cards = get_cards(text)
    target = next((c for c in cards if c["attrs"].get("handle") == handle), None)
    if not target or not target["attrs"].get("address"):
        print(f"Pas d'adresse email connue pour {handle}.")
        return
    address = target["attrs"]["address"]
    password = getpass.getpass(f"Mot de passe pour {SENDER} : ")
    try:
        imap = imaplib.IMAP4_SSL(IMAP_HOST, IMAP_PORT)
        imap.login(SENDER, password)
        imap.select("INBOX", readonly=True)
        typ, data = imap.search(None, f'(FROM "{address}")')
        if typ != "OK" or not data[0]:
            print(f"Aucun email trouve de {address}.")
            imap.logout()
            return
        last_id = data[0].split()[-1]
        typ, msg_data = imap.fetch(last_id, "(BODY.PEEK[])")
        imap.logout()
        if typ != "OK" or not msg_data or not msg_data[0]:
            print("Impossible de recuperer le message.")
            return
        msg = email_lib.message_from_bytes(msg_data[0][1])
        print(f"De : {decode_mime_header(msg.get('From'))}")
        print(f"Objet : {decode_mime_header(msg.get('Subject'))}")
        print(f"Date : {msg.get('Date')}")
        print("-" * 40)
        print(extract_plain_text(msg).strip())
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
        "en-pause": ("badge-en-pause", "En pause"),
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
    elif cmd == "check-inbox":
        cmd_check_inbox()
    elif cmd == "read" and len(sys.argv) == 3:
        cmd_read(sys.argv[2])
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
