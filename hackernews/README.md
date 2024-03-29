# EXPRESS NEWS PROJECT by Folorunso Timson

This is a Fullstack Django API task  given by [Dowstrademus](https://www.drattraderapp.com/).
The Technologies used are Python(Django, Django rest framework), HTML and CSS. DRF was my choice because it's faster, better and identified to be the standard practice.




## REQUIRED TASKS

  - [x] Use Django. Make a new virtualenv and pip install it;
  - [x] Make a scheduled job to sync the published news to a DB every 5 minutes. You can start with the latest 100 items, and sync every new item from there. Note: there are several types of news (items), with relations between them;
  - [x] Implement a view to list the latest news;
  - [x] Allow filtering by the type of item;
  - [x] Implement a search box for filtering by text;
  - [x] As there are hundreds of news you probably want to use pagination or lazy loading when you display them.

It is also important to expose an API so that our data can be consumed:

  - [x] GET  : List the items, allowing filters to be specified;
  - [x] POST  : Add new items to the database (not present in Hacker News);

- [x] Bonus

  - [x] Only display top-level items in the list, and display their children (comments, for example) on a detail page;
  - [x] In the API, allow updating and deleting items if they were created in the API (but never data that was retrieved from Hacker News);
  - [x] Be creative! :)
  
  
