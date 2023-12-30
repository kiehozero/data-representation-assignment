from flask import Flask, jsonify, render_template, request
import config
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host=config.keys['host'],
    user=config.keys['user'],
    password=config.keys['pw'],
    database=config.keys['db']
)

data = []


# Home page
@app.route('/')
def index():
    return render_template('static/index.html')


# Add card to collection
@app.route('/add_card', methods=['POST'])
def add_card():
    # Add the data to the DB
    print('Data created successfully')
    return render_template('static/index.html')


# Show collection
@app.route('/get', methods=['GET'])
def get_cards():
    return jsonify(data)


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

    return jsonify({'message': 'Data updated successfully'})


# Delete card from collection
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_card(index):
    # Delete the data at the specified index
    del data[index]
    return jsonify({'message': 'Card deleted.'})


if __name__ == '__main__':
    app.run(debug=True)
