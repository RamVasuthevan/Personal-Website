---
layout: post
title: "Verify Jekyll Minima Site on Mastodon"
image: "/assets/bitsbipsbricks/Mastodon-Verification/mastodon-elephant-logo.webp"
permalink: bitsbipsbricks/Mastodon-Verification
---

{% include image.html 
  name="mastodon-elephant-logo.webp" 
  alt="Mastodon elephant logo" 
  width="300px"
%}

<br>

On Mastodon, one way that you can prove that you are who you say you are is by verifying that you own your personal site. 

For example, on my [Mastodon account](https://mastodon.social/@RamVasuthevan), I have verified that I own [ramvasuthevan.ca](ramvasuthevan.ca) 

You prove that you own a page by having a link from that page to your Mastodon account with a [`rel="me"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/me) attribute. 

The two simplest ways to verify your site: 

1. Add an invisible `<link>` tag inside the `<head>` tag at the top page that you linked to like: 

```
<link rel="me" href="https://mastodon.social/@RamVasuthevan"> 
```

2. By adding a hyperlink to your Mastodon profile somewhere on the page, like:

```
<a rel="me" href="https://mastodon.social/@RamVasuthevan">Mastodon</a> 
```

Unfortunately, if you add your Mastodon profile to your config file like [this](https://mastodon.social/settings/profile): 

```
mastodon:
  - username: RamVasuthevan
    instance: mastodon.social
```


Minima 2.5 does not automatically add the `rel=me` attribute to the link in the footer of your site. And there is no [plans](https://github.com/jekyll/minima/issues/696#issuecomment-1357651146) to add automatic verfication until Minima 3.

But you can copy the [_includes/social.html](https://github.com/jekyll/minima/blob/2.5-stable/_includes/social.html) file and add it to your `_includes` file.

And then add a `rel="me"` attribute to the a href tag for Mastodon

Or you can just copy my [version]()

After adding the link to your page, go to [https://mastodon.social/settings/profile](https://mastodon.social/settings/profile) and add the page you want to verify as one of the extra fields. Make sure copy the link exactly as you added it your website (i.e. `https://mastodon.social/@RamVasuthevan`). 

Your profile must be updated after adding the rel-me link to your web page.  If you have added the link to your profile before, then try removing the link from your profile, saving, re-adding the link, and then saving again. (See [documentation](https://docs.joinmastodon.org/user/profile/#verification)).
