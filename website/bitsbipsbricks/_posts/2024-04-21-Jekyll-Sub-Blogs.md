---
layout: post
title:  "Create Jekyll Sub Blogs using only Liquid"
image: "/assets/bitsbipsbricks/Jekyll-Sub-Blogs/andrew-neel-cckf4TsHAuw-unsplash.jpg"
permalink: bitsbipsbricks/Jekyll-Sub-Blogs
---

<style>
  :not(pre) > code {
    background-color: #f4f4f4; /* Light grey background */
    color: #333; /* Darker text for better readability */
    padding: 2px 4px;
    border-radius: 4px;
  }
</style>

{% include unsplash_image.html 
   name="andrew-neel-cckf4TsHAuw-unsplash.jpg" 
   alt="Stock photo of a laptop, coffee, pen, notepad and phone" 
   photographer="Andrew Neel" 
   username="@andrewtneel" 
   image_link="https://unsplash.com/photos/macbook-pro-white-ceramic-mugand-black-smartphone-on-table-cckf4TsHAuw" 
%}

I started writing this [blog](/bitsbipsbricks.html) in the spirit of [Visa's do 100's things](https://www.visakanv.com/blog/do100things/). 

I started writing on [Ghost](https://ghost.org/) because it was easy to set up and maintain. At first, I didn't mention my name anywhere. Eventually, I decided to merge it with my personal site after I became more confident with my writing and so that I could gain more control over how the site looked. As an engineer, I love being able to take advantage of Git for version control, setting up my writing experience using VS Code and knowing that I can easily maintain and migrate it from Jekyll if necessary.

Jekyll by default puts all blog posts into one feed, but sometimes, I want to write something small, a [snippet](/snippets), a note mostly for myself, that doesn't really fit in [Bits, Bips and Bricks](/bitsbipsbricks).

By taking advantage of Jekyll categories and tags you can easy have multiple sub blogs each with their own Atom feed using only Liquid

A [category](https://jekyllrb.com/docs/posts/#categories) can be defined using the front matter keys `category` or `categories` (a space separated list of categories) or putting a directory above the post's `_post` directory with the name of the category. 

A [tag](https://jekyllrb.com/docs/posts/#tags) can be defined using can be defined using the front matter keys `tag` or `tags` (a space separated list of tags)

This snippet is built to match the style of Minma, but similar logic can be used for another theme. Download the file and save it in `_includes/blog.html`.

Copy the following code and paste it in `_includes/blog.html`:

{% highlight liquid %}
{% raw %}
<div class="blog">
    <h2 class="post-list-heading">{{ page.list_title | default: "Posts" }}</h2>
    <ul class="post-list">
      {%- for post in site.posts -%}
      {%- if post.categories contains include.category or post.tags contains include.tag -%}
      <li>
        {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
        <span class="post-meta">{{ post.date | date: date_format }}</span>
        <h3>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h3>
        {%- if site.show_excerpts -%}
          {{ post.excerpt }}
        {%- endif -%}
      </li>
      {%-endif -%}
      {%- endfor -%}

    </ul>

    {%- if include.category and site.feed.categories contains include.category -%}
      {% unless include.tag %}
      {% assign feed_location = site.feed.categories[include.category].path | default: '/feed/' | append: include.category | append: '.xml' | relative_url %}
        <p class="rss-subscribe">subscribe <a href="{{ '/feed/' | append: include.category | append: '.xml' | relative_url }}">via RSS</a></p>
        {% endunless %}
    {%- endif -%}

    {%- if include.tag and site.feed.tags contains include.tag -%}
    {% unless include.category %}
      <p class="rss-subscribe">subscribe <a href="{{ '/feed/' | append: include.tag | append: '.xml' | relative_url }}">via RSS</a></p>
    {% endunless %}
    {%- endif -%}

</div>
{% endraw %}
{% endhighlight %}

The above code is available under the MIT license and contains code from [minima/_layouts/home.html](https://github.com/jekyll/minima/blob/38a84a949f9753c4542e25f422935f59b4913053/_layouts/home.html)
<br><br>

On the page that you want a sub blog with only posts from a certain category:
{% highlight liquid %}
{% raw %}
{% include blog.html category="category_name" %}
{% endraw %}
{% endhighlight %}

On the page that you want a sub blog with only posts with a certain tag:
{% highlight liquid %}
{% raw %}
{% include blog.html tag="tag_name" %}
{% endraw %}
{% endhighlight %}

If you don't add a category or tag parameter, then all posts will be in the sub blog.

[Minima](https://github.com/jekyll/minima/pull/137/files#r124796175) assumes that if there are no posts, the feed will not be shown. I disagree, you can have a blog without blog posts. Update your *_config.yml* according to the instructions for [jekyll-feed](https://github.com/jekyll/jekyll-feed) to make sure that the feeds for your category or tag are generated.