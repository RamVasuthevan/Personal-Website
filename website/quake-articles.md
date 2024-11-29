---
layout: page
title: Quake Articles
---

Tyler Cowen has this idea of [quake books](https://marginalrevolution.com/marginalrevolution/2007/11/view-quake-read.html) — books that trigger an earthquake in how you view the world.

Most articles are fleeting, even good articles are a pale imitation of good books, but a great articles can change how you think about the world just as much as great books.


{% for quake in site.data.quake-articles %}
- [{{quake.title}}]({{quake.url}}) — {{quake.author}}
{% endfor %}