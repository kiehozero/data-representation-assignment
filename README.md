# Data Representation Assignment, Winter 2023/2024

A repository for the final assignment in ATU Data Representation, submitted in the winter 2023/24 semester.

## Project Outline

### Requirements

Create a Web application in Flask that has a RESTful API, the application should link to one or more database tables. Also create the web pages that can consume the API, i.e. performs CRUD operations on the data.

### Assessment strategy

1. Level 1 (40-45%): A basic Flask server that has a REST API, (to perform CRUD operations), one database table and accompanying web interface, using AJAX calls, to perform these CRUD operations
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

In the game itself, a MySQL table contains a number of pre-loaded players sourced from the statistical database endpoint above, and a user can pick which particular card and statistic they wish to play. A second  table in the same database contains a larger number of players, one of which is selected at random and presented visually as a second card. If the user's chosen card has a higher number in the chosen statistic, the user wins the other card and can choose whether to add it to the database.

## Technical Aspects

To get up and running I used a light [Bootstrap](https://getbootstrap.com/docs/4.1/getting-started/introduction/) template that I had previously created on a project called [Awayday](https://github.com/kiehozero/away-day), which is hosted [here](https://kiehozero.github.io/away-day/index.html). The Jinja2 templating engine that comes with [Flask](https://flask.palletsprojects.com/en/3.0.x/templating/) has been utilised just to reduce the number of HTML pages that require editing, and [jQuery](https://api.jquery.com/) provided a quick way to provide user interactivity. Pretty much all of the Bootstrap CSS styling and Flask interactivity on this website was taken from the Awayday project, with the occasional visit to ChatGPT when something wasn't working sufficiently.

The database is built on [MySQL](https://www.mysql.com/) and [PyMySQL](https://pypi.org/project/pymysql/) is used to communicate CRUD requests from Flask. The database tables are built using three Python files stored in the root directory of this repository. The first table, players, returns all of the player IDs from active player endpoint in the NHL API. The second table, 'all_players', then loops through a number of these players and calls the individual statistical player database using those IDs, and returns a wider stat selection. The third table has the same data, except it is the saved collection of cards that the player has won in the game. I initially populated this with six players just to get the game active and enable a random selection of cards.

### A Note on the API

The NHL changed a large number of endpoints and storage methods during Autumn 2023, causing a minor panic online among some users at [r/Hockey](https://www.reddit.com/r/hockey/) and some Discord channels that focus on hockey statistics. This API remains under revision by the league, and it looks like they have yet to fully re-structure the data in a uniform manner.

I've noticed for some players that 'position' is sometimes listed as 'positionCode', while others have differences between 'teamName' and 'fullTeamName', and not every player has a headshot photograph, ever if they've been in the league a while (i.e. Shea Weber!!!). I hoped to populate the all_players table with all of the active players, around 2200 entries, on the API, but after 116 players, an error was returned regarding a column that a particular player didn't have on the API. This number seemed like a sufficient amount to build the game around so I carried on without making any further amendments to the code.

There are also differences between column names in different tables, and some players taken from the active player list who do not show up in the player stats engine when their ID code is showing up. Included in the reference section are some discussions and ad-hoc documentation that third-party users noticed themselves, some of these discussions were of enormous use in getting this project off the ground, as the NHL have yet to release officialy documentation.

## Proposed Improvements and Bugfixess

At present the addAllPlayers function is run on an ad-hoc basis. An improvement here would be to implement a delete-and-insert process to perioducally recreate the table with the latest available players. If the script at present is run, it will simply add the same values, while deleting all records and starting again creates a new set of primary keys. At present, no records are updated from the API once they are added to the database for this project, so as the season progresses the likelihood of a user winning games will decrease, so a call to the API to replace stored players would become crucial.

The API hosts a lot of data and this product only references a few basic statistics, solely from the perspective that the higher number is better. An option to select a wider range of statistics for different positions, for example hits and blocks for defenders, or save percentage and shutouts for netminders, would more accurately reflect the value of each player's numbers. Indeed, there is currently a line in the database creation code that specifically excludes netminders as their core season statistics do not match those of all other positions.

A properly implemented star schema would become essential if more data was to be added to this product. At present the API call takes the team logo for each player, a star schema with team information will allow for more efficient storage of this data (storing it once for each 32 teams, rather than a team logo for all 2200 players).

A bug that I identified was that on the Assists, Points and Penalty Minutes categories, the comparison doesn't seem to work and produces a winning result each time. I looked through the jQuery and could not work this out, but deleting semi-colons from the end of if statements seemed to work, proving that I will never truly understand Javascript.

## References

### API Documentation

Bloodlinealpha (2023) "NHL Stats and Analysis Expert" [Github](https://github.com/bloodlinealpha/NHL-Stats-and-Analysis-Expert/blob/main/nhlAPI.json)
\
Hynes, D. (2023) "New API documentation" [Gitlab: nhl-api](https://gitlab.com/dword4/nhlapi/-/blob/master/new-api.md)
\
National Hockey League (2023) [Individual Player Statistics endpoint](https://api-web.nhle.com/v1/player/8477846/landing) (Note that I've pre-populated this link with a player ID)
\
National Hockey League (2023) [Master Player Directory endpoint](https://search.d3.nhle.com/api/v1/search/player?q=*&culture=en-us&limit=6000)
\
National Hockey League (2023) "NHL Stats". [NHL.com](https://www.nhl.com/stats/)
\
r/hockey (2003) "NHL Down - Looking for Alternatives". [Reddit](https://www.reddit.com/r/hockey/comments/17qu8by/nhl_api_down_looking_for_alternatives_software/)
\
Sidwar, K. (2023) "Reverse Engineering an API" [YouTube](https://www.youtube.com/watch?v=wjo68W2qkqw)
\
Zmalski (2023) "NHL API Reference" [Github](https://github.com/Zmalski/NHL-API-Reference)

### Core Documentation and Software

[Bootstrap documentation](https://getbootstrap.com/docs/4.1/getting-started/introduction/)
\
[Favicon Generator](https://favicon.io/favicon-converter/)
\
[Flask documentation](https://flask.palletsprojects.com/en/3.0.x/)
\
[Font Awesome](https://fontawesome.com/)
\
[Google Fonts](https://fonts.google.com/specimen/Titillium+Web)
\
[jQuery](https://api.jquery.com/)
\
[MySQL](https://www.mysql.com/)
\
[PyMySQL](https://pypi.org/project/pymysql/)
\
[PythonAnywhere](https://help.pythonanywhere.com/pages/Flask/)
\
[Requests Library](https://requests.readthedocs.io/en/latest/user/quickstart/)

### Code Help and Useful Tools

Beatty, A. (2003) "Data Representation" [Github](https://github.com/andrewbeattycourseware/datarepresentation)
\
[ChatGPT](https://chat.openai.com/)
\
[GitHub CoPilot](https://copilot.github.com/)
\
Flask documentation (2023) "Accessing request data in Flask". [Flask](https://flask.palletsprojects.com/en/3.0.x/quickstart/#accessing-request-data)
\
Flask documentation (2023) "Flash messages in Flask". [Flask](https://flask.palletsprojects.com/en/3.0.x/patterns/flashing/)
\
Flask documentation (2023) "Getting a Favicon to work in Flask". [Flask](https://flask.palletsprojects.com/en/1.1.x/patterns/favicon/)
\
Flask documentation (2023) "Templates in Flask". [Flask](https://flask.palletsprojects.com/en/3.0.x/tutorial/templates/)
\
Nishant, V. (2020) "Flask to MySQL setup". [AskPython](https://www.askpython.com/python-modules/flask/flask-mysql-database)
\
jQuery Documentation (2023) "jQuery text() method". [jQuery](https://api.jquery.com/text/)
\
Saint, S. (2022) "Awayday". [Github](https://github.com/kiehozero/away-day)
\
Saint, S. (2022) "Awayday". [Github Pages](https://kiehozero.github.io/away-day/index.html)
\
Technical Panchayat (2023) "Flask and PyMySQL: Introduction". [Medium](https://medium.com/@technicalpanchayat18/flask-pymysql-introduction-ae00ab1821f)
\
Technical Panchayat (2023) "Flask and PyMySQL: CRUD Operations". [Medium](https://medium.com/@technicalpanchayat18/flask-pymysql-crud-operations-93c279b84c4c)
\
User:'instanceof me' (2010) "How can I get the ID of an element using jQuery?" [StackOverflow](https://stackoverflow.com/questions/3239598/how-can-i-get-the-id-of-an-element-using-jquery#3239600)
\
W3Schools (2023) "jQuery attr() method". [W3Schools](https://www.w3schools.com/jquery/html_attr.asp)
\
W3Schools (2023) "jQuery toggle text". [W3Schools](https://www.w3schools.com/howto/howto_js_toggle_text.asp)
\
W3Schools (2023) "jQuery tutorial". [W3Schools](https://www.w3schools.com/jquery/default.asp)
