---
layout: page
title: Credits
permalink: /credits/
---

<table>
  <tr>
    <th>Item</th>
    <th>Link</th>
    <th>License</th>
  </tr>
{% for credit in site.data.credits %}
  <tr>
    <td><img src="{{credit.image}}" alt="{{credit.name}}" width="60" height="60"> </td>
    <td><a href="{{credit.link}}" target="_blank">{{credit.name}}</a></td>
    <td><a href="{{credit.license_link}}" target="_blank">{{credit.license_text}}</a></td>
  </tr>
{% endfor %}
</table>
