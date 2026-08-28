---
layout: post
title:  "SSG Digital Garden"
image: "/assets/snippets/Interchange-No Longer-on-Loan/Photo_of_Interchanged_by_Willem_de_Kooning.jpg"
permalink: snippets/SSG-Digital-Garden
categories: snippets
---

{% include image.html 
   src="/assets/snippets/Interchange-No Longer-on-Loan/Photo_of_Interchanged_by_Willem_de_Kooning.jpg" 
   alt="Photo of Interchange by Willem de Kooning taken by Andrew Cho"
   caption="Photo of Interchange by Willem de Kooning taken by [Andrew Cho/Wikipedia](https://en.wikipedia.org/wiki/File:Photo_of_Interchanged_by_Willem_de_Kooning.jpg)" 
%}

- I am very happy with personal website. It reduces the Activation energy of starting a new public writing or code project
- This started as [realestate.ramvasuthevan.ca](https://realestate.ramvasuthevan.ca/) built with clubber 
- Clubber 
   - simpple static site generator
   - thin wrapper over Pandocomatic (which itself is a wrapper around pandoc) and python server
- I deployed this website use CF pages
- I wanted to use this site to serve as a repository of offical documents (see https://realestate.ramvasuthevan.ca/toronto-community-housing-corporation) and my notes to intresting thing related to real esate
- I didn't think these things fit well on my blog
- Clubber and requiring a PR everytime feel constrainting
- I would quickly create an issue instead of updating the site


- I am looking to migrate to diffrent tool, to either create a public digital garden for all of my public notes or just real esate related note.
- One of the thing I live about Jeykll is the extendability.
   - I can extend it using Python to create data files [extract-toogoodtogo-invoices](https://github.com/RamVasuthevan/Personal-Website/tree/main/scripts/extract-toogoodtogo-invoices)
   - Use Github actions to update the source of my project
   - I much perfer Python to Ruby, if I really need to I can write my Jeykll plugins
- I want this tool for this site to be 
   - extendable (I am an software engineer, by extendable I mean I can write code for it)
   - content in markdown 
   - source in github
   - deployable to Clould Flare Pages
   - Will still be suported 10 years from now
   - Will be easy to work with
   - I should be able to copy and paste a link from any page

### Choices
- Obsidian Publish
- jekyll-garden.github.io
- simply-jekyll
- jekyll-bonsai
-  quartz (https://notes.joschua.io/)


Some more: https://github.com/MaggieAppleton/digital-gardeners

Inspired by: https://nicolasbouliane.com/blog/digital-gardening