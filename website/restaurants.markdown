---
layout: page
title: Restaurants Recommendations
---

<h1>My favorite restaurants in Toronto</h1>

{% for restaurant in site.data.restaurants %}
<div>
  <h2>{{ restaurant.name }}</h2>
  <p><strong>Category:</strong> {{ restaurant.category }}</p>
  <p><strong>Address:</strong> {{ restaurant.address }}</p>
  <p><strong>Website:</strong> <a href="{{ restaurant.website }}">{{ restaurant.website }}</a></p>
</div>
{% endfor %}
