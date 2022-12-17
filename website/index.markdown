---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

Hello 👋

I am a software engineer. I’m interested in technology, finance and real estate.  

<br>

<p align="center">
{% for highlight in site.data.highlights %}
<a href="{{highlight.link}}"><img src="{{highlight.image}}" width="60" height="60"></a>
{% endfor %}
</p>

<br>

Mos of my writing is an [Bits, Bips and Bricks](https://www.bitsbipsbricks.com/).

---

P.S. Why is this website so sparse?

I spent several years procrastinating on creating a personal website. Trying to create a good personal website using good tools with good content.

I was inspired by this [tweet](https://twitter.com/RamVasuthevan/status/1589036193966329856?s=20&t=ugmG3OLXRUIKGov6VA4zEQ) to actually just do it. We’ll see what improvements I make going forward.

Here is the [repo](https://github.com/RamVasuthevan/Personal-Website) for this website.