---
layout: page
title: Restaurants Recommendations
---

<h1>My favorite restaurants in Toronto</h1>

{% for restaurant in site.data.restaurants %}
<div>
  <h2><a href="{{restaurant.website}}" style="color: black; text-decoration: underline;">{{restaurant.name}}</a></h2>
  <p><strong>Category:</strong> {{ restaurant.category }}</p>
  <p><strong>Address:</strong> {{ restaurant.address }}</p>
  {% if restaurant.note %}
  <p><strong>Note:</strong> {{ restaurant.note }}</p>
  {% endif %}
</div>
{% endfor %}
