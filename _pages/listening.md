---
layout: page
permalink: /listening/
title: listening
nav: true
nav_order: 3
---

Since 2010, at the end of each year I have made a list of my favorite 10 or 20 albums from that year.

<div class="container">
  {% for entry in site.data.listening.list %}
  <div class="year-container">
    <div class="year">
      <h4>{{ entry.year }}</h4>
    </div>
    <div class="books">
	{% if entry.year == "2020 (unranked)" %}
      		<ul class="reading-list {{ entry.year }}">
        	{% for album in entry.albums %}
        		<li>{{ album.title }}<span class="author">by {{ album.artist }}</span></li>
        	{% endfor %}
      		</ul>
      	{% else %}
		<ol reversed class="reading-list {{ entry.year }}">
        		{% for album in entry.albums %}
        			<li>{{ album.title }}<span class="author">by {{ album.artist }}</span></li>
        		{% endfor %}
      		</ol>
	{% endif %}
    </div>
  </div>
  {% endfor %}
</div>
