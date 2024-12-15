from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_FILE = 'library.json'

def read_data():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def write_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/books', methods=['POST'])
def add_book():
    book = request.json
    if not all(k in book for k in ('title', 'author', 'published_year', 'isbn')):
        return jsonify({'error': 'Missing required fields'}), 400

    books = read_data()
    if any(b['isbn'] == book['isbn'] for b in books):
        return jsonify({'error': 'Book with this ISBN already exists'}), 409

    books.append(book)
    write_data(books)
    return jsonify({'message': 'Book added successfully'}), 201

@app.route('/books', methods=['GET'])
def list_books():
    books = read_data()
    return jsonify(books), 200

@app.route('/books/search', methods=['GET'])
def search_books():
    """Search for books by author, published year, or genre."""
    author = request.args.get('author')
    year = request.args.get('published_year')
    genre = request.args.get('genre')

    books = read_data()
    filtered_books = [
        book for book in books
        if (author is None or book['author'] == author) and
           (year is None or str(book['published_year']) == year) and
           (genre is None or book.get('genre') == genre)
    ]

    return jsonify(filtered_books), 200

@app.route('/books/<string:isbn>', methods=['DELETE'])
def delete_book(isbn):
    books = read_data()
    books = [book for book in books if book['isbn'] != isbn]
    write_data(books)
    return jsonify({'message': 'Book deleted successfully'}), 200

@app.route('/books/<string:isbn>', methods=['PUT'])
def update_book(isbn):
    update_data = request.json
    books = read_data()
    for book in books:
        if book['isbn'] == isbn:
            book.update(update_data)
            write_data(books)
            return jsonify({'message': 'Book updated successfully'}), 200

    return jsonify({'error': 'Book not found'}), 404

SWAGGER_URL = '/api-docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
