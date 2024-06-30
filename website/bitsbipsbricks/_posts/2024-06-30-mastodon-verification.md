---
layout: post
title: "Verify Jekyll Minima Site on Mastodon"
image: "/assets/bitsbipsbricks/Github-Dependabot-PRs/nolan-issac-It0DCaCBr40-unsplash.jpg"
permalink: bitsbipsbricks/XXX
---

{% include unsplash_image.html 
  name="nolan-issac-It0DCaCBr40-unsplash.jpg" 
  alt="Caffe latte on white ceramic cup beside silver and black laptop computer" 
  photographer="Nolan Issac" 
  username="@nolanissac" 
  image_link="https://unsplash.com/photos/caffe-latte-on-white-ceramic-cup-beside-silver-and-black-laptop-computer-It0DCaCBr40" 
%}

On Mastodon, one way that you can prove that you are who you say you are is by verifying that you own your personal site. 

For example, on my [Mastodon account](https://mastodon.social/@RamVasuthevan), I have verified that I own [ramvasuthevan.ca](ramvasuthevan.ca) 

You prove that you own a page by having a link from that page to your Mastodon account with a `rel="me"` attribute. 

Go to [https://mastodon.social/settings/profile](https://mastodon.social/settings/profile) and add the page you want to verify as one of the extra fields 

The two simplest ways to verify your site are to add an invisible link tag inside the <head> tag of the top page that you linked to like: 

```
<link rel="me" href="https://mastodon.social/@RamVasuthevan"> 
```

Or by adding a hyperlink to your mastodon profile somewhere on the page, like:

```
<a rel="me" href="https://mastodon.social/@RamVasuthevan">Mastodon</a> 
```


Unfortunately, if you add your Mastodon profile to your config file like [this](https://mastodon.social/settings/profile): 

```
mastodon:
  - username: RamVasuthevan
    instance: mastodon.social
```


Minima 2.5 does not automatically add the rel=me attribute to the link in the footer of your site. And there is no [plans](https://github.com/jekyll/minima/issues/696#issuecomment-1357651146) to add automatic verfication until Minima 3.

But you can copy the [_includes/social.html](https://github.com/jekyll/minima/blob/2.5-stable/_includes/social.html) file and add it to your _includes file .

And then add a `rel="me"` attribute to the a href tag for Mastodon

Or you can copy my [version]()