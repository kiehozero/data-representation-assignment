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


# Home page - return cards from each table in DB and renders to index.html
@app.route('/', methods=['GET'])
def index():
    cursor = db.cursor()
    # Generate a random player ID and retrieve player from collection
    col_count = '''SELECT COUNT(*) FROM collection'''
    cursor.execute(col_count)
    col_rows = cursor.fetchone()[0]
    rand_col = random.randint(1, col_rows)

    col_select = '''SELECT * FROM collection WHERE id = %s'''
    cursor.execute(col_select, rand_col)
    player_one = cursor.fetchone()

    cursor = db.cursor()
    # Generate a random player ID and retrieve player from all_players
    all_count = '''SELECT COUNT(*) FROM all_players'''
    cursor.execute(all_count)
    all_rows = cursor.fetchone()[0]
    rand_all = random.randint(1, all_rows)

    all_select = '''SELECT * FROM all_players WHERE id = %s'''
    cursor.execute(all_select, rand_all)
    player_two = cursor.fetchone()

    cursor.close()

    return render_template(
        'index.html',
        player_one=player_one, player_two=player_two)


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

# Add required data to dictionary
# reqdData = {
    # 'playerId': player_two[1],
    # 'first_name': player_two[2],
    # 'last_name': player_two[3],
    # 'position': player_two[4],
    # 'team': player_two[5],
    # 'logo_url': player_two[6],
    # 'headshot_url': player_two['headshot'],
    # 'games': player_two['seasonTotals'][-1]['gamesPlayed'],
    # 'goals': player_two['seasonTotals'][-1]['goals'],
    # 'assists': player_two['seasonTotals'][-1]['assists'],
    # 'points': player_two['seasonTotals'][-1]['points'],
    # 'penaltyMinutes': player_two['seasonTotals'][-1]['pim']
    # }


# Retrieve all cards from collection DB
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

    db.close()
    cursor.close()
    return render_template('collection.html', collection=collection)


# NOT DONE Delete card from collection
@app.route('/collection/<int:id>', methods=['DELETE'])
def delete_card(id):
    cursor = db.cursor()
    sql_delete = '''DELETE FROM collection WHERE id = %s'''
    cursor.execute(sql_delete, id)
    # Add flash confirming deletion
    print('Card deleted.')
    return redirect(url_for('collection'))


# NOT DONE (NOT MARKED), catch all for invalid URLs
@app.route('/invalid', methods=['GET'])
def invalid():
    # need a catch-all for invalid URLs
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
