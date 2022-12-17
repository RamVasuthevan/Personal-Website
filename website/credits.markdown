---
layout: page
title: Credit
permalink: /credit/
---

| Item | Link | License |   
| -- | -- | -- |
{% for credit in site.data.credits %}
|<img src="{{credit.image}}" alt="{{credit.name}}" width="60" height="60"> | [{{credit.name}}]({{credit.link}})  |[{{credit.license_text}}]({{credit.license_link}})|
{% endfor %}