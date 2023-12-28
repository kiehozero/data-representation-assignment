# Implement all the API calls as functions
import random
import requests

listUrl = "https://search.d3.nhle.com/api/v1/search/player?q=*&culture=en-us&limit=6000&active=true"
statUrl = "https://api-web.nhle.com/v1/player/"

playerIds = []
# this is the actual number of players in the DB as of 28/12/2023
lenPlayers = 2190


def getAllPlayers():
    response = requests.get(listUrl)
    # Andrew's note: in production you would check the status code each time
    players = response.json()
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
    randPlayer = random.randint(0, lenPlayers)
    chosenPlayer = playerIds[randPlayer]
    landing = "/landing"
    callRandPlayer = statUrl + str(chosenPlayer) + landing
    response = requests.get(callRandPlayer)
    randPlayerData = response.json()
    reqdData = {'playerId': randPlayerData['playerId'],
                'firstName': randPlayerData['firstName'],
                'lastName': randPlayerData['lastName'],
                # sometimes this is position, not positionCode, this API is an
                # absolute mess, only seems to be for ID 8482515 so far
                'position': randPlayerData['position'],
                'fullTeamName': randPlayerData['fullTeamName'],
                'teamLogo': randPlayerData['teamLogo']}
    print(reqdData)


def createBook(book):
    response = requests.post(url, json=book)
    return response.json()


def updateBook(id, bookdiff):
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()


def deleteBook(id):
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
