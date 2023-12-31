# data-representation-assignment

A repository for the final assignment in ATU Data Representation, submitted in the winter 2023/24 semester.

## Project requirements

Requirements:

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

## Overview of Completed Project

The final product in this assignment is a Top Trumps-style game that takes data from the statistical records of the National Hockey League. The League pushes a large amount of in-game and aggregated data to a number of APIs, hosted at [NHL Stats](https://www.nhl.com/stats/) and [NHL Edge](https://edge.nhl.com/). For the sake of this assignment, I accessed the active player API ([endpoint](https://search.d3.nhle.com/api/v1/search/player?q=*&culture=en-us&limit=6000)) and the individual statistical player database ([endpoint](https://api-web.nhle.com/v1/player/8477846/landing)). The inspiration for this project originally came from [Upper Deck E-Pack](https://www.upperdeckepack.com/), a website where users can collect and trade sports and entertainment trading cards, after I attended an ice hockey game in Sweden and scanned a QR code for some free cards.

In the game itself, a MySQL database contains a number of pre-loaded players, and a user can pick which particular card and statistic they wish to play. The latter API is then called to return a randomised player's statistics, which are presented visually as a second card. If the user's chosen card has a higher number in the chosen statistic, the user wins the other card and can choose whether to add it to the database.

- CREATE/UPDATE: if you win you get to the add the card to your collection, ability to choose favourites which appear at the top of the list?
- DELETE: can delete cards from your collection

## Technical Aspects

To get up and running I used a light [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) template that I had previously created on a project called [Awaydays](https://github.com/kiehozero/away-day), which is hosted [here](https://kiehozero.github.io/away-day/index.html). The Jinja2 templating engine that comes with Flask has been utilised just to reduce the number of HTML pages that require editing, and [jQuery](https://api.jquery.com/) provided a quick way to provide user interactivity.

- Flask, MySQL, hosting, etc., PyMySQL as I was having some trouble with mysql-connector

### A Note on the API

The NHL changed a large number of endpoints and storage methods during Autumn 2023, causing a minor panic online among some users at [r/Hockey](https://www.reddit.com/r/hockey/) and some Discord channels that focus on hockey statistics. This API remains under revision by the league, and it looks like they have yet to fully restructure the data in a uniform manner. I've noticed for some players that 'position' is sometimes listed as 'positionCode', while others have differences between 'teamName' and 'fullTeamName'. There are also differences between column names in different tables, and some players taken from the active player list who do not show up in the player stats engine when their ID code is showing up. Included in the reference section are some discussions and ad-hoc documentation that third-party users noticed themselves, some of these discussions were of enormous use in getting this project off the ground, as the NHL have yet to release officialy documentation.

## Proposed Improvements

At present the addAllPlayers function is run on an ad-hoc basis. An improvement here would be to implement a delete-and-insert process to perioducally recreate the table with the latest available players. If the script at present is run, it will simply add the same values, while deleting all records and starting again creates a new set of primary keys. At present, no records are updated from the API once they are added to the database for this project, so as the season progresses the likelihood of a user winning games will decrease, so a call to the API to replace stored players would become crucial.

The API hosts a lot of data and this product only references a few basic statistics, solely from the perspective that the higher number is better. An option to select a wider range of statistics for different positions, for example hits and blocks for defenders, or save percentage and shutouts for netminders, would more accurately reflect the value of each player's numbers. Indeed, there is currently a line in the database creation code that specifically excludes netminders as their core season statistics do not match those of all other positions.

A properly implemented star schema would become essential if more data was to be added to this product. At present the API call takes the team logo for each player, a star schema with team information will allow for more efficient storage of this data (storing it once for each 32 teams, rather than a team logo for all 2200 players).

## References

### API Documentation

[Active Player API endpoint](https://search.d3.nhle.com/api/v1/search/player?q=*&culture=en-us&limit=6000)
[individual statistical player database endpoint](https://api-web.nhle.com/v1/player/8477846/landing)

[Github documentation on NHL API](https://github.com/Zmalski/NHL-API-Reference) - this man is a lifesaver
[More NHL API documentation because the league can't be bothered writing it themselves](https://gitlab.com/dword4/nhlapi/-/blob/master/new-api.md)
[Discussion on the API and some general points](https://www.reddit.com/r/hockey/comments/17qu8by/nhl_api_down_looking_for_alternatives_software/?rdt=40503)
[NHL Stats and Analysis Expert](https://github.com/bloodlinealpha/NHL-Stats-and-Analysis-Expert/blob/main/nhlAPI.json) - this was useful for explaining some of the parameters rather than any actual ideas for the assignment
[NHL Stats](https://www.nhl.com/stats/)
[This video](https://www.youtube.com/watch?v=wjo68W2qkqw) helped immensely in pulling the API apart

### Core Documentation

[Bootstrap documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
[Flask docs](https://flask.palletsprojects.com/en/2.0.x/)
[jQuery](https://api.jquery.com/)
[PyMySQL](https://pypi.org/project/pymysql/)

### Code Help and Useful Tools

[ChatGPT](https://chat.openai.com/)
[GitHub CoPilot](https://copilot.github.com/)
[Getting a Favicon to work in Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/)
[Templates in Flask](https://flask.palletsprojects.com/en/1.1.x/tutorial/templates/)
[Accessing request data in Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data)
[Upper Deck E-Pack](https://www.upperdeckepack.com/) was my inspiration for doing a card-based game
W3 Schools'[jQuery tutorial](https://www.w3schools.com/jquery/default.asp) was simply invaluable. Javascript is by far my weakest skill in this course, pretty much every mistake I made in writing JS or jQuery code was fixed by a part of that tutorial.
[Favicon Generator](https://favicon.io/favicon-converter/)
[jQuery toggle text](https://www.w3schools.com/howto/howto_js_toggle_text.asp)
Technical Panchayat (2023) [Flask and PyMySQL: Introduction](https://medium.com/@technicalpanchayat18/flask-pymysql-introduction-ae00ab1821f)
Technical Panchayat (2023) [Flask and PyMySQL: CRUD Operations](https://medium.com/@technicalpanchayat18/flask-pymysql-crud-operations-93c279b84c4c)
[Google Fonts](https://fonts.google.com/specimen/Titillium+Web)
[Font Awesome](https://fontawesome.com/)
[here](https://kiehozero.github.io/away-day/index.html)
[Awaydays](https://github.com/kiehozero/away-day), which is hosted [here](https://kiehozero.github.io/away-day/index.html)
