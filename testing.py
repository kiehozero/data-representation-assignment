# Implement all the API calls as functions
import config
import pymysql
import random
import requests

listUrl = "https://search.d3.nhle.com/api/v1/search/player"
listquery = "?q=*&culture=en-us&limit=6000&active=true"
statUrl = "https://api-web.nhle.com/v1/player/"

# Database parameters
db = pymysql.connect(
    host=config.keys['host'],
    user=config.keys['user'],
    password=config.keys['pw'],
    database=config.keys['db']
)

# The actual number of players in the DB as of 28/12/2023
lenPlayers = 2190


# API call to get all players for DB population. Unused in the webpage.
def addAllPlayers():
    playerIds = []
    response = requests.get(listUrl + listquery)
    players = response.json()
    for player in players:
        playerIds.append(int(player["playerId"]))
    counter = 0

    cursor = db.cursor()
    # Add each player to the DB
    for i in playerIds:
        sql_insert = '''INSERT INTO players (player_id) VALUES (%s)'''
        cursor.execute(sql_insert, i)

        db.commit()
        counter += 1
    print(f'{counter} players added to collection')

    db.close()
    cursor.close()


def getRandPlayer(lenPlayers):
    # generate a random number between 0 and the length of the list of players
    # consider adding a try except, whereby if the player chosen is a goalie,
    # it will try again instead of using their data. This might be something
    # that can be passed to the initial SQL list, but that might require
    # converting the lists in getAllPlayers to dicts and changing things around
    # Once the GetAllPlayers items are stored in a DB, you can call the list
    # length from there without running that function first
    # needs functionality to loop through existing collection and return only
    # players not already in the collection
    randPlayer = random.randint(0, lenPlayers)
    # needs to be replaced with a call to DB or JSON?

    chosenPlayer = playerIds[randPlayer]
    landing = "/landing"
    callRandPlayer = statUrl + str(chosenPlayer) + landing
    response = requests.get(callRandPlayer)
    randPlayerData = response.json()
    # Add required data to dictionary
    reqdData = {'playerId': randPlayerData['playerId'],
                # Default items selected where multiple languages are available
                'firstName': randPlayerData['firstName']['default'],
                'lastName': randPlayerData['lastName']['default'],
                # Warning: occasionally this is positionCode, not positionCode
                'position': randPlayerData['position'],
                'fullTeamName': randPlayerData['fullTeamName']['default'],
                'teamLogo': randPlayerData['teamLogo'],
                'headshot': randPlayerData['headshot'],
                # Source stats for final season in seasonTotals dictionary
                'games': randPlayerData['seasonTotals'][-1]['gamesPlayed'],
                'goals': randPlayerData['seasonTotals'][-1]['goals'],
                'assists': randPlayerData['seasonTotals'][-1]['assists'],
                'points': randPlayerData['seasonTotals'][-1]['points'],
                'penaltyMinutes': randPlayerData['seasonTotals'][-1]['pim']
                }
    print(reqdData)


# Call all players from collection table in DB
def getCollection():
    pass


def addPlayer(player):
    response = requests.post(url, json=player)
    return response.json()


# def updateBook(id, bookdiff):
    # updateurl = url + "/" + str(id)
    # response = requests.put(updateurl, json=bookdiff)
    # return response.json()


def deletePlayer(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()


if __name__ == "__main__":
    book = {
        'Author': "Michel Foucault",
        'Title': "Discipline and Punish",
        'Price': 100
    }
    bookdiff = {
        'Price': 85
    }
    addAllPlayers()
    # getRandPlayer(lenPlayers)
    # print(createBook(book))
    # print(updateBook(345, bookdiff))
    # print(deleteBook(324))
