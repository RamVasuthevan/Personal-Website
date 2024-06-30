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

On Macedon, one way that you can prove that you are who you say you are is by verifying that you own your personal site. 

For example, on my master account, I have verified that I own ramvasuthevan.ca 

You prove that you owe your personal site by having a link from your site to your master account with a rel me attribute. 

Go to https://mastodon.social/settings/profile and add your personal site as one of the extra fields 

The two simple ways to verify your site are to add a link attribute inside <head> tag of the page that you linked to: 

<link rel="me" href="https://mastodon.social/@RamVasuthevan"> 

Or my adding a hyperlink to your mastodon profile somewhere on your homepage

<a rel="me" href="https://mastodon.social/@RamVasuthevan">Mastodon</a> 


Unfortunately, if you add your Mastodon profile to your config file like this 


Mania 2.5 does not automatically add a Rel equals me attribute, and will not Adderall equals me attribute until there is a release for many a 3.0 

but you can copy the _includes/social.html file and add it to your _includes file 


And then add  rel="me" to the a href tag site.mastodon

Or you can copy this version


https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/me
https://dev.to/tkuenneth/minima-mastodon-and-relme-1g7n
https://joinmastodon.org/verification