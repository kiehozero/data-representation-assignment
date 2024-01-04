from flask import (
    flash, Flask, jsonify, redirect, render_template, request, url_for)
import config
import pymysql
import random
import requests

app = Flask(__name__, static_url_path='', static_folder='static')

db = pymysql.connect(
    host=config.keys['host'],
    user=config.keys['user'],
    password=config.keys['pw'],
    database=config.keys['db']
)

# The actual number of players in the DB as of 28/12/2023
lenPlayers = 2190
# The number of players I managed to import before an error (see README)
storedPlayers = 115

data = []


# NOT DONE Home page
@app.route('/', methods=['GET'])
def index():
    mycard = []
    randcard = []
    # load all players from collection DB, add dropdowns
    # load random player from all_players DB
    return render_template('index.html', mycard=mycard, randcard=randcard)


# TEMPLATE FOR ABOVE Return card from collection
@app.route('/get/<int:id>', methods=['GET'])
def get_card(id):
    return jsonify(data[id])


# retrieve all cards from collection DB
@app.route('/collection', methods=['GET'])
def get_cards():
    collection = []
    cursor = db.cursor()
    sql_select = '''SELECT * FROM collection'''
    cursor.execute(sql_select)
    players = cursor.fetchall()
    for player in players:
        pl = list(player)
        collection.append(pl)
    return render_template('collection.html', collection=collection)


# NOT DONE Update - What can I do for an update operation?
@app.route('/collection/<int:id>', methods=['PUT'])
def update_card(index):
    # Get the updated data from the request
    updated_data = request.json

    # Update the data at the specified index
    data[index] = updated_data

    # Add flash confirming update
    print('Data updated successfully')
    return redirect(url_for('collection'))


# NOT DONE Delete card from collection
@app.route('/collection/<int:id>', methods=['DELETE'])
def delete_card(id):
    cursor = db.cursor()
    sql_delete = '''DELETE FROM collection WHERE id = %s'''
    cursor.exeter(sql_delete, id)
    # Add flash confirming deletion
    print('Card deleted.')
    return redirect(url_for('collection'))


# NOT DONE, MOVE TO GET_INDEX Retrieve a random player from all_players DB and return stats
def getRandPlayer(storedPlayers):
    randPlayer = random.randint(0, storedPlayers)
    cursor = db.cursor()

    # Retrieve player from DB
    sql_select = '''SELECT player_id FROM all_players WHERE id = %s'''
    cursor.execute(sql_select, randPlayer)
    chosenPlayer = cursor.fetchone()[0]

    # Add required data to dictionary
    reqdData = {
        'playerId': chosenPlayer['playerId'],
        # Default items selected where multiple languages are available
        'firstName': chosenPlayer['firstName']['default'],
        'lastName': chosenPlayer['lastName']['default'],
        'position': chosenPlayer['position'],
        'fullTeamName': chosenPlayer['fullTeamName']['default'],
        'teamLogo': chosenPlayer['teamLogo'],
        'headshot': chosenPlayer['headshot'],
        # Source stats for final season in seasonTotals dictionary
        'games': chosenPlayer['seasonTotals'][-1]['gamesPlayed'],
        'goals': chosenPlayer['seasonTotals'][-1]['goals'],
        'assists': chosenPlayer['seasonTotals'][-1]['assists'],
        'points': chosenPlayer['seasonTotals'][-1]['points'],
        'penaltyMinutes': chosenPlayer['seasonTotals'][-1]['pim']
    }
    print(reqdData)


# NOT DONE Add card to collection
@app.route('/add_card', methods=['POST'])
def add_card():
    # Add the data to the DB
    some_data = {'player_id': request.json["player_id"],
                 'player_name': request.json["player_name"]}
    print(some_data)
    '''data needs to be packaging up in the http request, and then in this
    function you would refer to that as request.json, with the data being in
    the form of a dictionary, so you'd have request.json['player_id'] etc.
    '''
    # Add flash confirming card added
    return redirect(url_for('index'))


# NOT DONE (NOT MARKED), catch all for invalid URLs
@app.route('/invalid', methods=['GET'])
def invalid():
    # need a catch-all for invalid URLs
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
