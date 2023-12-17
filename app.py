from flask import Flask, request, jsonify

app = Flask(__name__)

data = []


# Home page
@app.route('/')
def index():
    return "Hello NHL"


# Add card to collection
@app.route('/add', methods=['POST'])
def add_card():
    # Get the data from the request
    new_data = request.json

    # Add the data to the list
    data.append(new_data)

    return jsonify({'message': 'Data created successfully'})


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
