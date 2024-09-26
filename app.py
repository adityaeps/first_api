from flask import Flask,request,jsonify



app = Flask(__name__)

# Dummy data (could be anything, for example, user info)
dummy_data = [
    {'id': 1, 'name': 'John Doe', 'email': 'john.doe@example.com'},
    {'id': 2, 'name': 'Jane Smith', 'email': 'jane.smith@example.com'}
]

# Root endpoint
@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Dummy API'}), 200

# Get all dummy data
@app.route('/api/data', methods=['GET'])
def get_all_data():
    return jsonify(dummy_data), 200

# Get a single data entry by ID
@app.route('/api/data/<int:data_id>', methods=['GET'])
def get_data_by_id(data_id):
    entry = next((item for item in dummy_data if item['id'] == data_id), None)
    if entry:
        return jsonify(entry), 200
    else:
        return jsonify({'error': 'Data not found'}), 404

# Add new data
@app.route('/api/data', methods=['POST'])
def add_data():
    new_data = request.get_json()
    new_data['id'] = len(dummy_data) + 1
    dummy_data.append(new_data)
    return jsonify(new_data), 201

# Update data by ID
@app.route('/api/data/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    updated_data = request.get_json()
    entry = next((item for item in dummy_data if item['id'] == data_id), None)
    if entry:
        entry.update(updated_data)
        return jsonify(entry), 200
    else:
        return jsonify({'error': 'Data not found'}), 404

# Delete data by ID
@app.route('/api/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    entry = next((item for item in dummy_data if item['id'] == data_id), None)
    if entry:
        dummy_data.remove(entry)
        return jsonify({'message': 'Data deleted successfully'}), 200
    else:
        return jsonify({'error': 'Data not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
