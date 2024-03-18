---
layout: page
title: Git Scraping
---

[Git Scraping](https://simonwillison.net/2020/Oct/9/git-scraping/) inspired by Simon Willison. 

Download a file regularly using Git Actions, check it into Git and see how it changes over time.

### Scraping Project

<table>
<tbody>
<tr>
<td><strong>Projects</strong></td>
<td><strong>Notes</strong></td>
<td><strong>Updates</strong></td>
</tr>
{% for project in site.data.git-scraping %}
<tr>
<td>{{ project.name | markdownify | remove: '<p>' | remove: '</p>'}}</td>
<td>
  <ul>
    {% for note in project.notes %}
      <li>{{ note | markdownify | remove: '<p>' | remove: '</p>'}}</li>
    {% endfor %}
  </ul>
</td>
<td>{{ updated | markdownify | remove: '<p>' | remove: '</p>'}}</td>
</tr>
{% endfor %}
</tbody>
</table>
