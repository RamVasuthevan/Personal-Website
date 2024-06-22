---
layout: post
title:  "Search for all Dependabot Created PRs on your Repos"
image: "/assets/bitsbipsbricks/Jekyll-Sub-Blogs/andrew-neel-cckf4TsHAuw-unsplash.jpg"
permalink: bitsbipsbricks/Github-Dependabot-PRs
---

Search for all Dependabot Created PRs on your Repos  
Jun 22, 2024

In the spirit of early [patio11](https://www.kalzumeus.com/2006/), I’m going to write more about what I worked on, what I learned, and the problems I saw on any given day.

In that spirit, I have a bunch of repos with Dependabot enabled. It’s a pain in the ass to manually go to all of the repos and see if a Dependabot PR has been created.

<div>
  <label for="github-username">GitHub Username: </label>
  <input type="text" id="github-username" value="RamVasuthevan">
  <button onclick="updateQuery()">Search</button>
</div>

Search query: <code id="search-query">is:pr author:app/dependabot is:open archived:false owner:RamVasuthevan</code>

<p id="search-link">
  <a href="https://github.com/search?q=is%3Apr+author%3Aapp%2Fdependabot+is%3Aopen+archived%3Afalse+owner%3ARamVasuthevan">GitHub Search for Dependabot PRs</a>
</p>

<script>
  function updateQuery() {
    const username = document.getElementById('github-username').value;
    const query = `is:pr author:app/dependabot is:open archived:false owner:${username}`;
    const url = `https://github.com/search?q=${encodeURIComponent(query)}`;
    
    document.getElementById('search-query').innerText = query;
    document.getElementById('search-link').innerHTML = `<a href="${url}">GitHub Search for Dependabot PRs</a>`;
  }
</script>

This is a Jekyll blog post.
