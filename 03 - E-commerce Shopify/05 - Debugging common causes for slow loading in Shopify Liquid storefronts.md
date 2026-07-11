---
title: "Debugging common causes for slow loading in Shopify Liquid storefronts"
source: "https://performance.shopify.com/blogs/blog/debugging-common-causes-for-slow-loading-in-shopify-liquid-storefronts"
author:
  - "[[Sia Karamalegos]]"
published: 2024-01-11
created: 2026-06-20
description: "Have you ever been confronted with the daunting task of figuring out what exactly is causing a page to load slowly? Each page can suffer from hundreds of potential issues when it comes to page loading speed. Maybe you’ve experienced this first-hand with an endlessly long Lighthouse audit. No one wants to try optimizing"
tags:
  - "clippings"
---
Have you ever been confronted with the daunting task of figuring out what exactly is causing a page to load slowly? Each page can suffer from hundreds of potential issues when it comes to page loading speed. Maybe you’ve experienced this first-hand with an endlessly long Lighthouse audit. No one wants to try optimizing 10 different things to find out that none of them worked.

I am here to tell you that there is a better way. We can use real-user monitoring (RUM) data to provide directional clues that narrow down the possibilities. We work with Shopify merchants and theme developers on a daily basis and have seen the most common issues with Shopify sites.

In this article, I describe how to use this technique to analyze your RUM data. Then, I’ll provide you with a list of some of the most common speed issues for Shopify sites, broken down by those “directional clues”.

Spend more of your time understanding the first section which discusses the RUM analysis technique. Then, use the “common causes” section of this article as a reference after you identify your RUM problem areas. On wider screens, you should be able to see a quick navigation menu to the right.

Before we get started, let’s review the metrics…

## What are the Loading Speed Metrics?

The loading speed of a website is measured using three primary metrics, including Time to First Byte (TTFB), First Contentful Paint (FCP), and Largest Contentful Paint (LCP):

- **TTFB** is the time from when the user first requests the page to when the browser first receives a byte of data from the server.
- **FCP** has the same starting point as TTFB and ends when the first page content is rendered on the screen.
- **LCP** also has the same starting point as TTFB and ends when the largest text block or image element is fully visible to the user.

Since they all have the same starting point, you can visualize their timing like this:

![Chevrons showing how TTFB, FCP, and LCP overlap each other with the length of the chevron equal to their relative times for the good threshold](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/TTFB-FCP-LCP.png?width=1520)

TTFB, FCP, and LCP all have the same start time (when the request starts), but different ending times. A good TTFB occurs within 0.8 s, a good FCP occurs within 1.8 s, and a good LCP occurs within 2.5 s.

## Identifying Performance Gaps

LCP is one of the Core Web Vitals and has the biggest impact on user experience, with FCP at a close second. However, we still measure TTFB and FCP because they make up important parts of LCP and thus can help us understand better where things might be going wrong.

By looking at which metrics are failing the most or where the biggest performance “gaps” lie between them, we can more easily narrow down the potential causes. We like to call these “directional clues”. For example:

- A slow TTFB with FCP and LCP coming fairly quickly afterwards would suggest an issue with server response times. For Shopify sites, one cause could be complex Liquid code.
- A fast TTFB with a slow FCP and LCP coming fairly quickly after FCP suggests an issue with initial rendering. For Shopify sites, one cause could be anti-flicker snippets.
- Fast TTFB and FCP with an LCP coming in much later suggests an issue unique to the LCP element. One common issue we see is a lazy-loaded LCP image.

Let’s take a look at how these might look with RUM data. In the following visual examples, I’m using screenshots from the free [TREO sitespeed tool](https://treo.sh/sitespeed/) which uses the [Chrome User Experience Report (CrUX)](https://developer.chrome.com/docs/crux) API public data set.

When it comes to your site’s performance, not every page is the same! Ideally, you’d use your own analytics data and evaluate each page type (home, product, collection, etc.) and mobile vs desktop separately to narrow down your clues even further.

### What good looks like

Before you can compare yourself, you have to know what good looks like. This merchant performs excellently in all three page speed metrics:

![TREO distribution charts for TTFB, FCP, and LCP, and all show good/green](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/good-speed.png?width=1520)

### Poor FCP

In this example, we see TTFB is excellent, well within the “good” threshold of 0.8s. However, there is a 4.3 second gap until FCP. LCP is technically also poor, but it happens only 0.3 seconds after FCP indicating that FCP is the primary problem for this merchant.

![TREO distribution charts for TTFB, FCP, and LCP. TTFB is green, FCP and LCP are red](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/bad-fcp.png?width=1520)

### Poor FCP + LCP

Unfortunately, sometimes you can have multiple problems. In this case, TTFB is fast, FCP is somewhat slow, and LCP is poor. In this case I would optimize FCP first, then LCP though I’d still look for any obvious LCP issues early, like a lazy-loaded image.

![TREO distribution charts for TTFB, FCP, and LCP. TTFB is green, FCP is yellow, and LCP is red](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/bad-fcp-lcp.png?width=1520)

### Poor LCP

In this case, we’re back to an easier issue to sort out. Both TTFB and FCP are good. Only LCP needs to be optimized.

![TREO distribution charts for TTFB, FCP, and LCP. TTFB and FCP are green, and LCP is red](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/bad-lcp.png?width=1520)

### Poor TTFB

Up until this point, I’ve shown you all real examples from Shopify stores. However, when it comes to TTFB, it’s rare to come across a Shopify store with a very bad TTFB. Contrary to some beliefs, [Liquid storefronts are very fast](https://performance.shopify.com/blogs/blog/liquid-vs-headless-a-look-at-real-user-web-performance). However, if you are in the rare spot where you do have poor TTFB but the gaps before FCP and LCP are good, it might look something like this:

![TREO distribution charts for TTFB, FCP, and LCP. TTFB and FCP are yellow, and LCP is green](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/bad-ttfb.png?width=1520)

## Common causes for slow loading on Shopify

Now that you’ve identified the gaps for your site, what do you do next? In the following sections, I go over the common causes for slow performance on Shopify for each of the three loading speed metrics. These are not the only possible problems, just the most common ones. If you’re not on Shopify or have your own headless implementation, then unfortunately the list is longer.

Here is a summary of the the most common issues by gap metric which are detailed in the following sections:

**TTFB issues**

- [Complex Liquid](#complex-liquid)
- [Temporary Shopify server issues](#temporary-shopify-server-issues)

**LCP issues**

### TTFB issues

#### Complex Liquid

Liquid is the templating language used on Shopify, and our engineers are constantly improving Liquid rendering performance on our backend. However, a few problems can trip you up.

Complex liquid code from nested loops (loops within loops) or calling more data than you need can make Liquid rendering slow. In one edge case, I saw a merchant overuse product metadata with hundreds of checks on the product page for those metadata properties.

**What it looks like:**

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/Flame_graph_10_items_cart_rendering_time_124_ms.webp?width=1520)

The Theme Inspector flame graph shows a nested loop (repeated bars within a repeated bar) which is slowing down the Liquid rendering time.

This complexity can be inadvertent. You may be calling data that you do not need. In those cases, you can simplify the code and recover the performance.

In the cases where you need the complexity, you may want to re-architect the solution. For example, if you have a mega menu that requires complex Liquid and loops, you might consider rendering what's visible right away with Liquid and then using minimal JavaScript to fetch the rest of the data asynchronously. This would preserve the user’s perception of speed.

In any case, use the [Theme Inspector](https://shopify.engineering/in-depth-liquid-render-analysis-shopify-theme-inspector-chrome-extension) to determine if Liquid is your problem and how exactly it is rendering.

#### Temporary Shopify server issues

Other than Liquid complexity, achieving good TTFB is out of your control. Shopify has a dedicated team working on server optimizations and making Liquid faster, making it [best-in-class for server performance](https://performance.shopify.com/blogs/blog/liquid-vs-headless-a-look-at-real-user-web-performance#shopify-liquid-storefronts-are-fast-for-real-users). However, sometimes things go wrong. If your TTFB performance has dropped recently along with several other Shopify sites, then this might be the issue. These events are rare and usually recover quickly.

### FCP issues

#### Render blocking resources

As a browser parses HTML, it pauses when it encounters a link to a CSS or synchronous JavaScript file. The browser must then download these files before it can continue rendering the rest of the page.

**What it looks like:**

When running Lighthouse or [PageSpeed Insights](https://pagespeed.web.dev/), you will get a failed audit that looks like this:

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/render-blocking-lighthouse.png?width=1520)

Failed Lighthouse audit for render-blocking resources

The goal isn't to eliminate all render-blocking resources. For instance, CSS that styles content above the fold should be render-blocking. This prevents layout shifts or flashes of unstyled content.

On the other hand, JavaScript files, unless they are needed for rendering (such as in an A/B test or when using JavaScript to render the page with React or Vue), should often be deferred.

#### Anti-flicker snippets

Anti-flicker snippets are used to prevent a flash of unstyled content (FOUC) or a flash of original content (FOOC) when running A/B tests. They forcibly hide the page until some trigger point defined in JavaScript. However, forcibly hiding the page impacts performance so it’s a pretty big tradeoff. Andy Davies covers these tradeoffs and some options in his post [The Case Against Anti-Flicker Snippets](https://andydavies.me/blog/2020/11/16/the-case-against-anti-flicker-snippets/).

**What it looks like:**

Anti-flicker snippets can be tricky to find. Your first clue will be that FCP does not occur until well after the HTML and CSS downloads, which are lines 1-2 in the following waterfall. At this point, I usually suspect an anti-flicker snippet by looking for familiar script names. Here, the scripts from `www.googleoptimize.com` and `dev.visualwebsi…izer.com` were a clue that VWO (an A/B testing provider) was used. Then I tested disabling that script to validate that the FCP would occur faster.

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/anti-flicker.png?width=1520)

A waterfall chart from WebPageTest showing the green FCP line occurring around 2.75 sections when the blue HTML bar in line 1 was complete before 1.2 seconds. An HTML-first website without JavaScript rendering should render pretty quickly after the HTML and CSS are loaded.

If you use A/B testing, remember to close out tests once they are complete and ensure your testing app disables the anti-flicker snippet when no tests are running. If you customized your theme to add a third-party A/B testing library, you can encapsulate the script in a Liquid if statement that checks a theme setting toggle that completely removes the code when no testing is desired:

In `config/settings_schema.json`:

```json
{
 "name": "Third parties",
 "settings": [
   {
     "type": "checkbox",
     "id": "enable_vwo",
     "label": "Enable VWO Async SmartCode (for A/B testing)",
     "default": false
   }
 ]
},
```

In `layout/theme.liquid`:

```html
{% if settings.enable_vwo %}
 <!-- script for 3rd-party A/B testing provider like the VWO Async SmartCode -->
{% endif %}
```

#### Connections to multiple domains for critical assets

When a browser fetches resources like CSS, JavaScript, or images from different domains, it has to establish new connections. Each of these connections involves a DNS lookup, initial connection, and SSL negotiation before content can finally download. This added time can significantly slow down the FCP and LCP.

**What it looks like:**

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/multiple-domains.png?width=1520)

In this waterfall from WebPageTest, we can see that at least 9 domains are needed to connect to for critical assets before First Contentful Paint (the narrower orange/pink bars are new connections).

It’s best to limit the number of different domains the browser needs to connect to when loading a page. [Host your assets on the Shopify CDN](https://performance.shopify.com/blogs/blog/using-shopify-cdn-for-better-performance) (Content Delivery Network) as much as possible. In some cases where the external domain is unavoidable, you may be able to [use the `preconnect` resource hint](https://performance.shopify.com/blogs/blog/introduction-to-resource-hints#warming-up-connections-with-preconnect) to improve speed.

#### Overuse of preloads and fetchpriority=“high”

In the performance community, we often call preload a footgun because it’s easy to shoot yourself in the foot with it. You should not preload resources which are already referenced in the HTML file. This is a common misconception. The browser’s preload scanner will already be able to find them quickly.

**What it looks like:**

I created a [bookmarklet](https://projects.sia.codes/priorities-bookmarklet/) to help you quickly see all your preloads and fetchpriorities in one scan. You want to make sure that the list of elements with fetchpriority set to high and preloaded assets are minimal. We generally try to keep both under 2 each, but this is not a hard and fast rule. Always test before and after using a tool like WebPageTest to see which case is fastest.

Preloading is a powerful tool that instructs the browser to download a resource before it knows that it is needed. For example, when setting fonts in a CSS file, the browser will not know that it needs that font until quite late. That font may benefit from a preload.

On the other hand, blanket-applying preloads to any important resource usually leads to bandwidth contention, as too many resources are fighting for the same network resources. This can delay the loading of more important resources which are needed for both FCP and LCP.

Similarly, setting a high fetch priority can help ensure that critical resources are downloaded quickly. However, if too many resources are marked with a high fetch priority, it can confuse the browser's resource prioritization system. If every resource is important, then no resource is important.

Browsers are pretty smart when it comes to prioritizing content needed to render the page. Always test before and after adding a preload or a fetch priority to make sure that it actually improved the loading speed. Moderation is usually best.

#### Huge HTML

One popular pattern in ecommerce is large “mega menus” with hundreds and even thousands of DOM elements. On top of that, instead of using CSS to change the styling on mobile vs desktop, often a website will have 2 versions of the mega menu doubling the number of DOM elements.

**What it looks like:**

Here’s an example website which has two separate very large mega menus. The mobile nav contains 2,868 DOM nodes and the desktop nav contains 2,223. That’s over 5,000 nodes just for the nav on a page with 6,800 total nodes.

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/double-mega-menu.png?width=1520)

For this site, the Dev Tools inspector shows the mobile nav in the blue highlighted nav while the desktop version is in the grey highlighted nav.

In the Chrome Dev Tools inspector, you can get the DOM size contained within an element by selecting that element, then running `$0.querySelectorAll('*').length`. `$0` is the Chrome Dev Tools shorthand for the currently selected element.

Excessive DOM size is not usually a major culprit when it comes to loading speed except in these cases. If it is an issue for you, it's crucial to simplify the HTML where possible. Some options include:

- Architecting your mobile and desktop menus to use the same markup and vary the design using modern CSS features
- Render what’s immediately visible using Liquid and HTML then use JavaScript to fetch the rest of the data and render in the background. You should keep at least one menu rendered on the server to help with web search bots.

### LCP issues

#### Lazy loading the LCP image

Lazy loading is a technique where images are loaded only when they are near the viewport. This can improve performance by reducing the amount of data that needs to be loaded when the page is first requested.

However, if the LCP image is lazy loaded, it can significantly delay the LCP metric. This is because the image will not start to load until after the page is rendered and JavaScript can fire the [IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/httparchive_lcp_impact.png?width=1520)

Shopify sites that lazy load their LCP image have a median LCP that is 1.0 second slower than the eager loaded ones. Read more about lazy loading and its impact on performance.

**What it looks like:**

```html
<!-- Native lazy loading has a loading="lazy" attribute -->
<img src="photo.jpg" alt="" loading="lazy">

<!-- Lazy loading using a JavaScript library often has a class with 
    "lazy" in the name and data-src attributes -->
<img src="placeholder.jpg" data-src="photo.jpg" alt="" class="lazyloaded">
```

The [loading priorities scanner bookmarklet](https://projects.sia.codes/priorities-bookmarklet/) I created also checks the LCP code for the loading attribute and common attributes for lazy loading libraries shown above.

Use the new Liquid features of `section.index` and default lazy loading of the `image_tag` to vary loading strategies for images above the fold. Learn more about these plus code examples in our [article](https://performance.shopify.com/blogs/blog/announcing-new-liquid-features-for-better-web-performance).

A corollary to this is to not use auto-sizes for LCP images. This is a feature of some lazy loading libraries and in the works to be a native web feature. For the browser to be able to download the correct image eagerly, it needs a proper sizes attribute. If you use auto-sizes or the wrong sizes attribute, a new, larger image may be downloaded later, slowing down the LCP. Use the [Responsive Image Linter](https://chromewebstore.google.com/detail/responsive-image-linter/mnddginionlghpblkimpdalcecpnbjln?pli=1) Chrome extension to help you get your sizes right.

**What it looks like:**

```html
<!-- In the future, native auto sizes will set the sizes
     attribute to "auto" -->
<img src="photo.jpg" alt="" sizes="auto" loading="lazy">

<!-- Today, this is possible using a JavaScript framework which 
     often will have a data-sizes attribute set to auto -->
<img src="placeholder.jpg" data-src="photo.jpg" data-sizes="auto" alt="" class="lazyloaded">
```

#### Transitions on the LCP image

Transitions, such as fade-ins or other animations, can delay the point at which the browser considers the LCP image to be fully rendered, even if the image itself loads quickly.

**What it looks like:**

This one is harder to catch. First, if you run WebPageTest, you will see the image finish loading well in advance of the LCP event. This will tell you that something is delaying it, but not what. You’ll have to dig in more to understand if it is something like an anti-flicker snippet or an image transition. Sometimes you can eyeball it to see if you observe a blur up effect, or you can modify the filmstrip settings down to 0.1s to observe it there, as in the screenshot below. You can also use Dev Tools to inspect the image or the image container’s CSS to look for clues such as an `opacity` property.

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/transition-on-lcp.png?width=1520)

For this WebPageTest run, the LCP event occurred at 8.7 seconds. However, the LCP image finished downloading around 7.6 seconds (line 77). For the Filmstrip Settings, I shortened the Thumbnail Interval down to 0.1s instead of 0.5s which visually made the transition more obvious. Then, I used Dev Tools to inspect the image and found the opacity and transition properties.

Instead of gradually showing the image with a fade-in or blur-in effect, it's better to have the image appear immediately. While animations can add visual appeal, they can also make the user experience feel slower if they delay when the image is shown. Read more about how we helped one merchant [Improve Largest Contentful Paint (LCP) by removing image transitions](https://performance.shopify.com/blogs/blog/improve-largest-contentful-paint-lcp-by-removing-image-transitions).

#### Late discovered images

When an image is discovered late, the browser doesn't know to start downloading it until after it has finished parsing the CSS or JavaScript that references it. This can delay the loading of the image, causing a slower LCP.

**What it looks like:**

This typically happens in two cases:

1. When an image is referenced in a CSS file as a background image
2. When an image is loaded via JavaScript (via a framework or a complex image component)

In the mock-up below, you can see that in the case of a late discovered image, each file “chains” off the previous file which is why these are also called [critical request chains](https://developer.chrome.com/docs/lighthouse/performance/critical-request-chains):

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/late-discovered.png?width=1520)

Make sure your LCP image is discoverable in the HTML document, otherwise your LCP timing will take a hit.

To prevent this, reduce or remove the chain by using the `image_tag` in Liquid HTML files whenever possible. Favor code that can render what the page initially looks like fully in HTML and CSS, then layer in the dynamic behavior features using JavaScript.

#### Using JavaScript for rendering

When JavaScript is used to render pages, the browser has to wait for the JavaScript file to be downloaded and executed before it can start rendering the page. This can significantly delay the time it takes for content to appear on the screen.

**What it looks like:**

Disable JavaScript in your browser, then try loading your website. If all or most of the page does not render, you are likely either using JavaScript for rendering, or you have an anti-flicker snippet enabled.

Similar to other issues listed here, it’s best if you can use an HTML-first strategy for rendering. You can layer in any dynamic features with JavaScript afterwards. Yes, this means that using a frontend JavaScript framework like Vue or React with a Liquid storefront is going to make your site slower. It will also result in a worse [INP](https://performance.shopify.com/blogs/blog/announcing-inp-as-the-next-core-web-vital-what-shopify-stores-can-do-now).

We suggest deferring most JavaScript files, except when that script is needed for rendering, such as when running an A/B test. In these cases, deferring JavaScript would delay the rendering of the page even more.

```html
<!-- Defer non-critical JavaScript -->
<script src="non-critical.js" defer></script>
```

#### Cookie banners larger than main content

Cookie apps often display a banner or pop-up to inform users about the use of cookies on the site. These cookie pop-ups load late often because they are loaded via JavaScript. If the pop-up becomes the largest element in the viewport when it loads, it could become the LCP element, delaying the LCP event. Consider making the cookie banner smaller than the largest actual website element in the viewport.

**What it looks like:**

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/cookie-law.png?width=1520)

Both this cookie banner and its paragraph content are so large that it becomes the LCP for this page. Strive to reduce the content size to be less than the “true” LCP for the page.

#### Email and promotion pop-ups before user interaction

Similarly, newsletter modals and other types of pop-ups that appear before user interaction can become the LCP element and delay the LCP event.

**What it looks like:**

![](https://cdn.shopify.com/s/files/1/0657/6730/9530/files/subscribe-modal.png?width=1520)

An email subscription sign up form that appears before interacting with the page causing it to hijack the LCP event.

They often come from a third party or Shopify app and thus load quite late. Modals that ask for a user’s email address before they’ve even seen the page are also a user experience antipattern.

Most apps that offer this service have a setting where you can delay the pop up until after user interaction, such as scrolling. This way, the pop up won't become the LCP element, and the LCP metric will more accurately reflect the loading performance of the page's main content.

#### Incorrect prioritization

Similar to FCP, overusing preloads and fetch priority can impact the LCP element as well. They can lead to bandwidth contention, delaying the loading of more important resources. On the other hand, not setting `fetchpriority="high"` on the LCP image can result in the browser not prioritizing the download of this critical resource, leading to a slower LCP.

**What it looks like:**

I created a [bookmarklet](https://projects.sia.codes/priorities-bookmarklet/) to help you quickly see all your preloads and fetchpriorities in one scan. You want to make sure that the list of elements with fetchpriority set to high and preloaded assets are minimal. 2 or fewer of each is usually okay, but always test especially if you start going higher.

While preloading resources and setting a high fetch priority can be beneficial, they should be used judiciously. The key is to prioritize the right resources, not all resources.

## Conclusion

Now that you know how to identify the performance gaps and find their common causes, you can start optimizing the loading speed of your page in a more strategic way. In this article, you learned about the most common issues we see for each of those performance gaps. It’s not an exhaustive list, but it covers the cases we see most frequently.

Web performance is not easy. It requires understanding various metrics, identifying patterns, and asking the right questions. However, with practice and the right tools and a more efficient process, you can achieve a faster loading speed.

Header photo by [Marten Newhall](https://unsplash.com/@laughayette?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/person-using-magnifying-glass-enlarging-the-appearance-of-his-nose-and-sunglasses-uAFjFsMS3YY?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

**CONTENTS**

- [What are the Loading Speed Metrics?](#what-are-the-loading-speed-metrics%3F)
- [Identifying Performance Gaps](#identifying-performance-gaps)
- [What good looks like](#what-good-looks-like)
- [Poor FCP](#poor-fcp)
- [Poor FCP + LCP](#poor-fcp-%2B-lcp)
- [Poor LCP](#poor-lcp)
- [Poor TTFB](#poor-ttfb)
- [Common causes for slow loading on Shopify](#common-causes-for-slow-loading-on-shopify)
- [TTFB issues](#ttfb-issues)
- [FCP issues](#fcp-issues)
- [LCP issues](#lcp-issues)
- [Conclusion](#conclusion)