---
layout: page
title: Book Wish List
---

I currently use Amazon to track by book wish list.

Amazon Wish List

Advantages:
- Amazon wish lists will be supported forever
- Buy most of my books on Amazon 
- Tracks day when the book as addded to the wish list

Disadvantages:
- My wish list is split across Amazon.com and Amazon.ca
- No way to note why I added the book to wish list
- No way to easily tag books or categorize them 
- Closely linked with Amazon

read.gift
[https://read.gift/u/visakanv](https://web.archive.org/web/20220620200845/https://read.gift/u/visakanv)

OpenLibrary Book list
- This looks like what I am searching for but I still can't add the reason why I added to the list

Todo:
- Copy over Book list from Amazon

<h1>Books I want to read:</h1>

{% for wish in site.data.book-wish-list %}
<div>
    <h4>{{wish.name}}</h4>
    {%if wish.author.first %}
    <p>By: {{ wish.author | array_to_sentence_string}}</p>
    {% else %}
    <p>By: {{ wish.author }}</p>
    {% endif %}
    <p>Buy: <a href="https://www.amazon.com/dp/{{wish.isbn-10}}/">Amazon US</a> <a href="https://www.amazon.ca/dp/{{wish.isbn-10}}/">Amazon Canada</a></p>
    <p>Date Added: {{wish.date_added}}</p>
    <p>Reason Added: {{wish.reason_added | markdownify | remove: '<p>' | remove: '</p>'}}</p>
</div>
{% endfor %}