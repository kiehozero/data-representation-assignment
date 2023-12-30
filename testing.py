# Implement all the API calls as functions
import config
import pymysql
import random
import requests

listUrl = "https://search.d3.nhle.com/api/v1/search/player"
listquery = "?q=*&culture=en-us&limit=6000&active=true"
statUrl = "https://api-web.nhle.com/v1/player/"

playerIds = []
# this is the actual number of players in the DB as of 28/12/2023
lenPlayers = 2190


# can be removed once the DB is populated, cols in DB are:
# id(pk auto_inc), player_id, first_name, last_name, position,
# team, logo_url, headshot_url, gp, goals, assists, points, pim
def getAllPlayers():
    response = requests.get(listUrl + listquery)
    # Andrew's note: in production you would check the status code each time
    players = response.json()
    # print(players)
    for player in players:
        # need to strip out goalies
        playerIds.append(int(player["playerId"]))
    # you don't need to calculate the lenPlayers if it always calling stored
    # DB data, you'd only need to do this on refresh and player count changes
    return lenPlayers


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
    getAllPlayers()
    getRandPlayer(lenPlayers)
    # print(createBook(book))
    # print(updateBook(345, bookdiff))
    # print(deleteBook(324))
