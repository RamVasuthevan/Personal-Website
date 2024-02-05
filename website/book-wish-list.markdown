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
- There are book notes, which are private. I could use that as the reason I want to read abook. But reason there is now way in the UI to see all of the book notes at once

Todo:
- Copy over Book list from Amazon
- This is not data dense enough, make I should use a table

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
    {% if wish.recommendation %}
    <p>Where I found: {{wish.recommendation | markdownify | remove: '<p>' | remove: '</p>'}}</p>
    {% endif %}
    <p>Reason Added: {{wish.reason_added | markdownify | remove: '<p>' | remove: '</p>'}}</p>
</div>
{% endfor %}


<table>
    <tr>
      <th>Title</th>
      <th>Author</th>
      <th>Recommendation</th>
      <th>Reason Added</th>
      <th>Date Added</th>
    </tr>
    {% for book in site.data.book-wish-list %}
    <tr>
        <td style="word-wrap: break-word; max-width: 150px;">{{book.name}}</td>
        <td style="word-wrap: break-word; max-width: 150px;">{{book.author}}</td>
        <td style="word-wrap: break-word; max-width: 150px;">{{book.recommendation  | markdownify | remove: '<p>' | remove: '</p>'}}</td>
        <td style="word-wrap: break-word; max-width: 150px;">{{book.reason_added  | markdownify | remove: '<p>' | remove: '</p>'}}</td>
        <td style="word-wrap: break-word; max-width: 150px;">{{book.date_added}}</td>
    </tr>
    {% endfor %}
</table>
