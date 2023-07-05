---
layout: page
permalink: /reading/
title: reading
description: books I've read
nav: true
nav_order: 1
---

Since 2013, I have kept a list each year of the books that I read. These are 
archived here: [2023](/books/2023.html), [2022](/books/2022.html), [2021](/books/2021.html), 
[2020](/books/2020.html), [2019](/books/2019.html), [2018](/books/2018.html), 
[2017](/books/2017.html), [2016](/books/2016.html), [2015](/books/2015.html), 

<div class="container">
  <div class="last-update">Last updated {{ site.data.reading.lastupdate }}</div>
  {% for entry in site.data.reading.list %}
  <div class="year-container">
    <div class="year">
      <h4>{{ entry.year }}</h4>
      <div class="number">{{ entry.books | size }} books</div>
    </div>
    <div class="books">
      <ul class="reading-list {{ entry.year }}">
        {% for book in entry.books %}
        <li>
          {{ book.title }}
          <span class="author">by {{ book.author }}</span
          >{% if book.star %}<span class="star">★</span>{% endif %}
	  <span class="author">{% if book.year %}[{{ book.year}}]{% endif %}</span>
        </li>
        {% endfor %}
      </ul>
    </div>
  </div>
  {% endfor %}
</div>
