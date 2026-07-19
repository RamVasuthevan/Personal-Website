---
layout: page
title: Interesting YouTube Channels
---

## Channels

<ul style="margin-bottom: 0;">
{%- for channel in site.data.interesting-youtube-channels -%}
{%- if channel.display_on_page -%}
<li style="margin: 0;">
  <a href="{{ channel.channel_url }}">{{ channel.channel_name }}</a>
  {%- if channel.videos -%}
  <ul style="margin-top: 0.25em; margin-bottom: 0;">
    {%- for video in channel.videos -%}
    <li style="margin: 0;"><a href="{{ video.url }}">{{ video.title }}</a></li>
    {%- endfor -%}
  </ul>
  {%- endif -%}
</li>
{%- endif -%}
{%- endfor -%}
</ul>

## Videos

<ul style="margin-bottom: 0;">
{%- for video in site.data.interesting-youtube-videos -%}
{%- if video.display_on_page -%}
<li style="margin: 0;"><a href="{{ video.video_url }}">{{ video.video_title }}</a> by <a href="{{ video.channel_url }}">{{ video.channel_name }}</a></li>
{%- endif -%}
{%- endfor -%}
</ul>
