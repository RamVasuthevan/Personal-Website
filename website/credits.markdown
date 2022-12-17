---
layout: page
title: Credit
permalink: /credit/
---

{% for highlight in site.data.highlights %}
<table>
  <tr>
    <th>Item</th>
    <th>Link</th>
    <th>License</th>
  </tr>
  <tr>
    <td><img src="{{credit.image}}" alt="{{credit.name}}" width="60" height="60"> </td>
    <td><a href="{{credit.link}}">{{credit.name}}}}</a></td>
    <td><a href="{{credit.license_link}}">{{credit.license_text}}</a></td>
  </tr>
</table>
{% endfor %}