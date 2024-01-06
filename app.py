from flask import (
    Flask, redirect, render_template, request, url_for)
import config
import pymysql
import random

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

    return render_template(
        'index.html',
        player_one=player_one, player_two=player_two)


# NOT DONE Add card to collection
@app.route('/', methods=['POST'])
def add_card():
    # Add the data to the DB
    card = [
        request.json['player_id'],
        request.json['first_name'],
        request.json['last_name'],
        request.json['position'],
        request.json['team'],
        request.json['logo_url'],
        request.json['headshot_url'],
        request.json['gp'],
        request.json['goals'],
        request.json['assists'],
        request.json['points'],
        request.json['pim']
    ]

    cursor = db.cursor()
    card_insert = '''INSERT INTO collection (player_id, first_name,
        last_name, position, team, logo_url, headshot_url, gp, goals, assists,
        points, pim) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
    cursor.execute(card_insert, card)

    db.commit()
    print("1 record inserted, ID:", cursor.lastrowid)


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


if __name__ == '__main__':
    app.run(debug=True)
