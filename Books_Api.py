from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {
        'id': 1,
        'title': 'Python for Beginners',
        'author': 'John Smith'
    },
    {
        'id': 2,
        'title': 'Advanced Python',
        'author': 'Jane Doe'
    }
]


# Route to get all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)


# Route to get a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404


# Route to add a new book
@app.route('/books', methods=['POST'])
def add_book():
    new_book = {
        'id': request.json['id'],
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201


# Route to update an existing book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        book['title'] = request.json['title']
        book['author'] = request.json['author']
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404


# Route to delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        books.remove(book)
        return jsonify({'message': 'Book deleted'})
    else:
        return jsonify({'error': 'Book not found'}), 404


# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5004)
