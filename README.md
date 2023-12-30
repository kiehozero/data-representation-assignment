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

## Improvements

- currently storing the team logo URL in the player DB. Setting up a star schema with team information will allow for more efficient storage of this data (storing it once for each 32 teams, rather than a team logo for all 2200 players)
- at present there addAllPlayers function has to be run on an ad-hoc basis. A quick improvement here would be to implete a 'delete and insert' (get ref) process to perioducally recreate the table with the latest available data. If the script at preent is run, it will simply add the same values, and deleting all records and starting again creates a new set of primary keys
- add goalies

## References

[Bootstrap documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
[Github documentation on NHL API](https://github.com/Zmalski/NHL-API-Reference) - this man is a lifesaver
[More NHL API documentation because the league can't be bothered writing it themselves](https://gitlab.com/dword4/nhlapi/-/blob/master/new-api.md)
[Discussion on the API and some general points](https://www.reddit.com/r/hockey/comments/17qu8by/nhl_api_down_looking_for_alternatives_software/?rdt=40503)
[Getting a Favicon to work in Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/)
[Bootstrap dark mode](https://getbootstrap.com/docs/5.3/customize/color-modes/)
[Favicon Generator](https://favicon.io/favicon-converter/)
[NHL Stats and Analysis Expert](https://github.com/bloodlinealpha/NHL-Stats-and-Analysis-Expert/blob/main/nhlAPI.json) - this was useful for explaining some of the parameters rather than any actual ideas for the assignment
[This video](https://www.youtube.com/watch?v=wjo68W2qkqw) helped immensely in pulling the API apart
[Upper Deck E-Pack](https://www.upperdeckepack.com/) was my inspiration
W3 Schools'[jQuery tutorial](https://www.w3schools.com/jquery/default.asp) was simply invaluable. Javascript is by far my weakest skill in this course, pretty much every mistake I made in writing JS or jQuery code was fixed by a part of that tutorial.
[jQuery toggle text](https://www.w3schools.com/howto/howto_js_toggle_text.asp)
Technical Panchayat (2023) [Flask and PyMySQL: Introduction](https://medium.com/@technicalpanchayat18/flask-pymysql-introduction-ae00ab1821f)
Technical Panchatay (2023) [Flask and PyMySQL: CRUD Operations](https://medium.com/@technicalpanchayat18/flask-pymysql-crud-operations-93c279b84c4c)

- mention somewhere that the NHL changed their API without notice in October and sent a wave of panic through the r/hockey sub-reddit listed above, but some of the above docs helped everyone get back on track
- To get up and running I used a light Bootstrap template that I had previously created on a project called [Awaydays](https://github.com/kiehozero/away-day), which is hosted [here](https://kiehozero.github.io/away-day/index.html)