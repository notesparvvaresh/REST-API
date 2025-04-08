from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "TEST1", "author": "TEST1"},
    {"id": 2, "title": "1984", "author":  "George Orwell"},
]


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)



@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404
    


@app.route('/books', methods=['POST'])
def add_book():  
    data = request.get_json()
    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"]
    }
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        book.update({
            "title": data.get("title", book["title"]),
            "author": data.get("author", book["author"])
        })
        return jsonify(book)
    else:
        return jsonify({"error": "Book not found"}), 404


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global booksC
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 204


if __name__ == '__main__':
    app.run(debug=True)