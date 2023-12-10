from flask import Flask, request, jsonify

app = Flask(__name__)


# Create a list to store the data
data = []


# Create
@app.route('/create', methods=['POST'])
def create():
    # Get the data from the request
    new_data = request.json

    # Add the data to the list
    data.append(new_data)

    return jsonify({'message': 'Data created successfully'})


# Read
@app.route('/read', methods=['GET'])
def read():
    return jsonify(data)


# Update
@app.route('/update/<int:index>', methods=['PUT'])
def update(index):
    # Get the updated data from the request
    updated_data = request.json

    # Update the data at the specified index
    data[index] = updated_data

    return jsonify({'message': 'Data updated successfully'})


# Delete
@app.route('/delete/<int:index>', methods=['DELETE'])
def delete(index):
    # Delete the data at the specified index
    del data[index]

    return jsonify({'message': 'Data deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)
