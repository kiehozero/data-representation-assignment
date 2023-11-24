# data-representation-assignment

A repository for the final assignment in ATU Data Representation

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

- NHL Sportradar (reqs API key)
- create a Top Trumps game?
- start with random player
- user picks one of five or six items from stats (G, A, Shots, Hits, +/-?)
- click PLAY to reveal card and win/loss
- CREATE/UPDATE: if you win you get to the add the card to your collection, ability to create multiple squads of five?
- DELETE: can delete cards from your collection
- AUTH: register to save your cards
- link more information from Elite Prospects (reqs API key)? Looks like a bit of hassle getting a key here

idea 2:

- setlist.fm (reqs API key) called Last.fm, shows you a setlist so you can listen to the songs again? something rubbish like that
- replicate Bands spreadsheet as DB using setlist.fm data
- integrate Last.fm (reqs API key) and Spotify (reqs API key)? Looks like it has a weird authentication method in Last.fm, send artist or song to Spotify playlist?

style ideas:

- [Bootstrap dark mode](https://getbootstrap.com/docs/5.3/customize/color-modes/)
