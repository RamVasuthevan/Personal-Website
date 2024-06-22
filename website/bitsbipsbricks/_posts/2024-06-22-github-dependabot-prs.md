---
layout: post
title: "Search for All Dependabot Created PRs on Your Repos"
image: "/assets/bitsbipsbricks/Github-Dependabot-PRs/nolan-issac-It0DCaCBr40-unsplash.jpg"
permalink: bitsbipsbricks/Github-Dependabot-PRs
---

{% include unsplash_image.html 
  name="nolan-issac-It0DCaCBr40-unsplash.jpg" 
  alt="Caffe latte on white ceramic cup beside silver and black laptop computer" 
  photographer="Nolan Issac" 
  username="@nolanissac" 
  image_link="https://unsplash.com/photos/caffe-latte-on-white-ceramic-cup-beside-silver-and-black-laptop-computer-It0DCaCBr40" 
%}

In the spirit of early [patio11](https://www.kalzumeus.com/2006/), I’m going to write more about what I worked on, what I learned, and the problems I solved on any given day.

In that spirit, I have a bunch of repos with Dependabot enabled. It’s a pain in the ass to manually go to all of the repos and see if a Dependabot PR has been created.

Search query: <code id="search-query">is:pr author:app/dependabot is:open archived:false user:@me</code>

<a href="https://github.com/search?q=is%3Apr+author%3Aapp%2Fdependabot+is%3Aopen+archived%3Afalse+user%3A%40me&type=pullrequests" target="_blank">GitHub Search for Dependabot PRs</a>
