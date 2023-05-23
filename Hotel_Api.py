from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
hotels = [
    {
        'id': 1,
        'name': 'Hotel A',
        'city': 'City A',
        'price': 100
    },
    {
        'id': 2,
        'name': 'Hotel B',
        'city': 'City B',
        'price': 150
    },
    {
        'id': 3,
        'name': 'Hotel C',
        'city': 'City C',
        'price': 200
    }
]


# Routes
@app.route('/hotels', methods=['GET'])
def get_hotels():
    return jsonify(hotels)


@app.route('/hotels/<int:hotel_id>', methods=['GET'])
def get_hotel(hotel_id):
    hotel = next((hotel for hotel in hotels if hotel['id'] == hotel_id), None)
    if hotel:
        return jsonify(hotel)
    return jsonify({'message': 'Hotel not found'}), 404


@app.route('/hotels', methods=['POST'])
def create_hotel():
    data = request.get_json()
    if not data or 'name' not in data or 'city' not in data or 'price' not in data:
        return jsonify({'message': 'Invalid request'}), 400

    new_hotel = {
        'id': len(hotels) + 1,
        'name': data['name'],
        'city': data['city'],
        'price': data['price']
    }
    hotels.append(new_hotel)
    return jsonify(new_hotel), 201


@app.route('/hotels/<int:hotel_id>', methods=['PUT'])
def update_hotel(hotel_id):
    hotel = next((hotel for hotel in hotels if hotel['id'] == hotel_id), None)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404

    data = request.get_json()
    if not data or 'name' not in data or 'city' not in data or 'price' not in data:
        return jsonify({'message': 'Invalid request'}), 400

    hotel['name'] = data['name']
    hotel['city'] = data['city']
    hotel['price'] = data['price']
    return jsonify(hotel)


@app.route('/hotels/<int:hotel_id>', methods=['DELETE'])
def delete_hotel(hotel_id):
    hotel = next((hotel for hotel in hotels if hotel['id'] == hotel_id), None)
    if not hotel:
        return jsonify({'message': 'Hotel not found'}), 404

    hotels.remove(hotel)
    return jsonify({'message': 'Hotel deleted'})


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5005)
