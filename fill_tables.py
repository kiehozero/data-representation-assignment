# Implement all the NHL API calls as functions to the server
import config
import pymysql
import random
import requests

'''API URLs - listUrl is used to populate the DB, statUrl is used to get player
stats. The list contains top-line information on every player, mainly
biographical. The statUrl contains more detailed information on each player and
has to be called player-by-player. '''
listUrl = 'https://search.d3.nhle.com/api/v1/search/player'
listquery = '?q=*&culture=en-us&limit=6000&active=true'
statUrl = 'https://api-web.nhle.com/v1/player/'

# Database parameters
db = pymysql.connect(
    host=config.keys['host'],
    user=config.keys['user'],
    password=config.keys['pw'],
    database=config.keys['db'])

# The actual number of players in the DB as of 28/12/2023
lenPlayers = 2190


# API call to get all players for DB population
def addPlayerIds():
    playerIds = []
    response = requests.get(listUrl + listquery)
    players = response.json()
    for player in players:
        # BUGFIX: exclude goaltenders as they don't have the same stats.
        if player['positionCode'] == 'G':
            pass
        else:
            playerIds.append(int(player['playerId']))

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


# Retrieve all players from collection table and return stats from API
def addPlayerStats():
    cursor = db.cursor()
    sql_select = '''SELECT player_id FROM players LIMIT 20'''
    cursor.execute(sql_select)
    players = cursor.fetchall()
    for player in players:
        # API call to get player data
        callPlayer = statUrl + str(player[0]) + '/landing'
        response = requests.get(callPlayer)
        playerData = response.json()

        # Add required data to dictionary
        reqdData = {
            'playerId': playerData['playerId'],
            # Default items selected where multiple languages are available
            'firstName': playerData['firstName']['default'],
            'lastName': playerData['lastName']['default'],
            'position': playerData['position'],
            'fullTeamName': playerData['fullTeamName']['default'],
            'teamLogo': playerData['teamLogo'],
            'headshot': playerData['headshot'],
            # Source stats for final season in seasonTotals dictionary
            'games': playerData['seasonTotals'][-1]['gamesPlayed'],
            'goals': playerData['seasonTotals'][-1]['goals'],
            'assists': playerData['seasonTotals'][-1]['assists'],
            'points': playerData['seasonTotals'][-1]['points'],
            'penaltyMinutes': playerData['seasonTotals'][-1]['pim']
        }
        print(reqdData)
    db.cursor()
    db.close()


# Retrieve a random player from DB and return stats from API call
def getRandPlayer(lenPlayers):
    randPlayer = random.randint(0, lenPlayers)
    cursor = db.cursor()

    # Retrieve player from DB
    sql_select = '''SELECT player_id FROM players WHERE id = %s'''
    cursor.execute(sql_select, randPlayer)
    chosenPlayer = cursor.fetchone()[0]

    # API call to get player data
    callRandPlayer = statUrl + str(chosenPlayer) + '/landing'
    response = requests.get(callRandPlayer)
    randPlayerData = response.json()

    # Add required data to dictionary
    reqdData = {
        'playerId': randPlayerData['playerId'],
        # Default items selected where multiple languages are available
        'firstName': randPlayerData['firstName']['default'],
        'lastName': randPlayerData['lastName']['default'],
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
    collection = []
    cursor = db.cursor()
    sql_select = '''SELECT * FROM collection'''
    cursor.execute(sql_select)
    players = cursor.fetchall()
    # Convert to lists without Primary Key
    for player in players:
        pl = list(player)
        pl.pop(0)
        collection.append(pl)
    return collection


if __name__ == '__main__':
    book = {
        'Author': 'Michel Foucault',
        'Title': 'Discipline and Punish',
        'Price': 100
    }
    bookdiff = {
        'Price': 85
    }
    # addPlayerIds()
    addPlayerStats()
    # getRandPlayer(lenPlayers)
    # getCollection()

    # print(createBook(book))
    # print(updateBook(345, bookdiff))
    # print(deleteBook(324))
