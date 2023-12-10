# data-representation-assignment

A repository for the final assignment in ATU Data Representation, submitted in the winter 2023/24 semester.

## Project requirements

Requirements:
Write a program that demonstrates that you understand creating and consuming RESTful APIs.
If you cannot think of a project to do:

- Create a Web application in Flask that has a RESTful API, the application should link to one or more database tables.
- You should also create the web pages that can consume the API. I.e. performs CRUD operations on the data.

Assessment strategy:

1. Level 1 (40-45%): A rehash of the sample project lab. A basic Flask server that has a REST API, (to perform CRUD operations), one database table and accompanying web interface, using AJAX calls, to perform these CRUD operations
2. Level 2 (45-50%): As above, with more than one database table
3. Level 3 (50-55%): As above, with authorisation (logging in) 50%-55%

Plus (each point 0-10%):
4. The web page looks nice
5. A more complicated API
6. Server links to some third-party API
7. If the third-party API requires authentication
8. Hosted online (e.g. Azure, Pythonanywhere)

idea 1:

- NHL Top Trumps
- start with random player
- user picks one of five or six items from stats (G, A, Shots, Hits, +/-?)
- click PLAY to reveal card and win/loss
- CREATE/UPDATE: if you win you get to the add the card to your collection, ability to create multiple squads of five?
- DELETE: can delete cards from your collection
- AUTH: register to save your cards
- link more information from Elite Prospects (reqs API key)? Looks like a bit of hassle getting a key here

## References

[Bootstrap documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
[Github documentation on NHL API](https://github.com/Zmalski/NHL-API-Reference)
[More NHL API documentation because the league can't be bothered writing it themselves](https://gitlab.com/dword4/nhlapi/-/blob/master/new-api.md)
[Discussion on the API and some general points](https://www.reddit.com/r/hockey/comments/17qu8by/nhl_api_down_looking_for_alternatives_software/?rdt=40503)

 [Bootstrap dark mode](https://getbootstrap.com/docs/5.3/customize/color-modes/)

- mention somewhere that the NHL changed their API without notice in October and sent a wave of panic through the r/hockey sub-reddit, but some of the above docs helped everyone get back on track
