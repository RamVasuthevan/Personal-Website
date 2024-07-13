---
layout: post
title: "Twitter Cards Images are Cached"
image: "/assets/bitsbipsbricks/Mastodon-Verification/mastodon-elephant-logo-wider.webp"
permalink: bitsbipsbricks/Twitter-Cards-Cached
---

{% include image.html 
  name="mastodon-elephant-logo.webp" 
  alt="Mastodon elephant logo" 
  width="300px"
%}

<br>

[Yesterday, I learned](https://x.com/search?q=%22Today%20I%20learned%22%20OR%20TIL%20from%3ARamVasuthevan&src=typed_query&f=top) in a not-so-enjoyable fashion that Twitter caches [summary card images](https://developer.x.com/en/docs/twitter-for-websites/cards/overview/summary-card-with-large-image). 

While writing [Verify Jekyll Minima Site on Mastodon](/bitsbipsbricks/Mastodon-Verification), I originally had a summary card image which was getting cropped poorly, so I kept the image that was being displayed at the top of the article but changed the summary card image with a wider version which got a better crop. And it showed up correctly in my preferred Twitter Card preview tool: [BannerBear Twitter Card Preview Tool](https://www.bannerbear.com/tools/twitter-card-preview-tool/). 

{% include image.html 
  name="Screenshot 2024-07-13 at 3.50.56 PM.png" 
  width="300px"
%}

But when I posted it to Twitter, the old image would show up both when I actually posted it and in the preview when I was composing it. 

<br>

<div style="display: flex; align-items: flex-end; justify-content: center;">
    {% assign directory = page.permalink %}
    <img src="/assets/{{ directory }}/Screenshot%202024-07-13%20at%202.54.40%E2%80%AFPM.png" alt="Image 1" style="width: 300px; margin-right: 5px;">
    <img src="/assets/{{ directory }}/Screenshot%202024-07-13%20at%203.50.53%E2%80%AFPM.png" alt="Image 2" style="width: 300px;">
</div>


After some frustrating troubleshooting, I found this [support forum thread](https://devcommunity.x.com/t/twitter-summary-cards-are-they-cached/18345) that said Twitter caches summary images are cached for about a week, and the [preview tool](https://cards-dev.twitter.com/validator) could be used to expire the cache. 

And while the preview tool, no longer actually shows you a twitter preview, it does bust the cache.


{% include image.html 
  name="Screenshot%202024-07-13%20at%204.43.36%E2%80%AFPM.png" 
%}
