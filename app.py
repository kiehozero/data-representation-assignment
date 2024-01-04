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

data = []


# Home page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def asjson():
    book = {
        "player": request.json["player_id"],
        "player_ID": request.json["player_name"]
    }
    return jsonify(book)


# Add card to collection
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


# Show collection
@app.route('/collection', methods=['GET'])
def get_cards():
    return render_template('collection.html')


# Return card from collection
@app.route('/get/<int:id>', methods=['GET'])
def get_card(id):
    return jsonify(data[id])


# Update - What can I do for an update operation?
@app.route('/collection/<int:id>', methods=['PUT'])
def update_card(index):
    # Get the updated data from the request
    updated_data = request.json

    # Update the data at the specified index
    data[index] = updated_data

    # Add flash confirming update
    print('Data updated successfully')
    return redirect(url_for('collection'))


# Delete card from collection
@app.route('/collection/<int:id>', methods=['DELETE'])
def delete_card(index):
    # Delete the data at the specified index
    del data[index]
    # Add flash confirming deletion
    print('Card deleted.')
    return redirect(url_for('collection'))


# Retrieve a random player from all_players DB and return stats
def getRandPlayer(storedPlayers):
    randPlayer = random.randint(0, storedPlayers)
    cursor = db.cursor()

    # Retrieve player from DB
    sql_select = '''SELECT player_id FROM all_players WHERE id = %s'''
    cursor.execute(sql_select, randPlayer)
    chosenPlayer = cursor.fetchone()[0]

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


# Call all players from collection table in DB - move to app.py
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



@app.route('/invalid', methods=['GET'])
def invalid():
    # need a catch-all for invalid URLs
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
