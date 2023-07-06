---
layout: page
permalink: /reading/
title: reading
nav: true
nav_order: 1
---

What follows is a list of the books I have read since 2013, when I first started
keeping these lists. A star indicates a book that I think was very good, that I recommend, 
or that has stuck with me over the years.

<div class="container">
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
          <span class="author">by {{ book.author }}</span>
	  <span class="author">{% if book.year %}[{{ book.year}}]{% endif %}</span>
	  {% if book.star %}<span class="star">★</span>{% endif %}
        </li>
        {% endfor %}
      </ul>
    </div>
  </div>
  {% endfor %}
</div>
