---
layout: page
title: YouTube I Like
---
{% assign channels = site.data.youtube-channels %}
{% assign videos = site.data.youtube-videos %}

## Channels
{% for channel in channels %}
<div class="channel">
  <h3><a href="{{ channel.url }}" target="_blank">{{ channel.channel }}</a></h3>
  {% if channel.why %}
    <p><strong>Why I like it:</strong> {{ channel.why }}</p>
  {% endif %}
  {% if channel.sample-videos %}
    <h4>Sample Videos:</h4>
    <ul>
      {% for video in channel.sample-videos %}
        <li><a href="{{ video.url }}" target="_blank">{{ video.title }}</a></li>
      {% endfor %}
    </ul>
  {% endif %}
</div>
{% endfor %}

## Videos
{% for video in videos %}
<div class="video">
  <h3><a href="{{ video.url }}" target="_blank">{{ video.title }}</a> {% if video.channel_url and video.channel %}from <a href="{{ video.channel_url }}" target="_blank">{{ video.channel }}</a>{% endif %}</h3>
  {% if video.why != "" %}
    <p><strong>Why I like it:</strong> {{ video.why }}</p>
  {% endif %}
</div>
{% endfor %}
