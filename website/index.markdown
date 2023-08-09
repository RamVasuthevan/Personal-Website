---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
---

Hello 👋

I am a software engineer. I’m interested in technology, finance and real estate.

### **KPIs:**
{% assign current_date = 'now' | date: '%s' %}
{% assign last_published_date = site.data.bitsbipsbricks_rss_last_published_date | date: '%s' %}
{% assign difference_in_seconds = current_date | minus: last_published_date %}
{% assign difference_in_days = difference_in_seconds | divided_by: 86400 %}

Days since I've written for [Bits, Bips and Bricks](https://www.bitsbipsbricks.com/): {{ difference_in_days }}

### **What I am working on:**

<table class="table-first-col-nowrap">
  <tr>
    <th>Projects</th>
    <th>Description</th>
  </tr>
  {% for project in site.data.projects %}
  <tr>
    <td><a href="{{ project.url }}">{{ project.name }}</a></td>
    <td>{{ project.description }}</td>
  </tr>
  {% endfor %}
</table>

---

<br />

I spent several years procrastinating on creating a personal website. I was inspired by this [tweet](https://twitter.com/RamVasuthevan/status/1589036193966329856?s=20&t=ugmG3OLXRUIKGov6VA4zEQ) to actually just do it. Just put something up and go from there. Here is the [repo](https://github.com/RamVasuthevan/Personal-Website) for this website.
