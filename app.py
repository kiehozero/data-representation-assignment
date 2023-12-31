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
        "title": request.json["title"],
        "author": request.json["author"],
        "price": request.json["price"]
    }
    return jsonify(book)


# Add card to collection
@app.route('/add_card', methods=['POST'])
def add_card():
    # Add the data to the DB
    some_data = {'player_id': 1, 'player_name': 'John Doe'}
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
@app.route('/update/<int:id>', methods=['PUT'])
def update_card(index):
    # Get the updated data from the request
    updated_data = request.json

    # Update the data at the specified index
    data[index] = updated_data

    # Add flash confirming update
    print('Data updated successfully')
    return redirect(url_for('collection'))


# Delete card from collection
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_card(index):
    # Delete the data at the specified index
    del data[index]
    # Add flash confirming deletion
    print('Card deleted.')
    return redirect(url_for('collection'))


@app.route('/invalid', methods=['GET'])
def invalid():
    # need a catch-all for invalid URLs
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
