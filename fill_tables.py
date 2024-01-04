# Implement all the NHL API calls as functions to the server
import config
import pymysql
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
# The number of players I managed to import before an error (see README)
storedPlayers = 115


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


# Retrieve players from collection table and return stats from API
def addPlayerStats():
    cursor = db.cursor()
    sql_select = '''SELECT player_id FROM players'''
    cursor.execute(sql_select)
    players = cursor.fetchall()
    for player in players:
        # API call to get player data
        callPlayer = statUrl + str(player[0]) + '/landing'
        response = requests.get(callPlayer)
        playerData = response.json()

        '''Add required items to list and push to MySQL Default items selected
        where multiple languages are available. Source stats for final season
        in seasonTotals dictionary.'''
        reqdData = [playerData['playerId'], playerData['firstName']['default'],
                    playerData['lastName']['default'],
                    playerData['position'],
                    # Error on this item documented in README
                    playerData['fullTeamName']['default'],
                    playerData['teamLogo'], playerData['headshot'],
                    playerData['seasonTotals'][-1]['gamesPlayed'],
                    playerData['seasonTotals'][-1]['goals'],
                    playerData['seasonTotals'][-1]['assists'],
                    playerData['seasonTotals'][-1]['points'],
                    playerData['seasonTotals'][-1]['pim']]
        print(reqdData)

        sql_insert = '''INSERT INTO all_players (player_id, first_name,
        last_name, position, team, logo_url, headshot_url, gp, goals, assists,
        points, pim) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        cursor.execute(sql_insert, reqdData)
        db.commit()
        print('1 player added to collection, ID:', cursor.lastrowid)

    db.cursor()
    db.close()


if __name__ == '__main__':
    addPlayerIds()
    addPlayerStats()
