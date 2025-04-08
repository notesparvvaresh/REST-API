```bash
➜  ~ curl http://localhost:5000/books

[
  {
    "author": "TEST1",
    "id": 1,
    "title": "TEST1"
  },
  {
    "author": "George Orwell",
    "id": 2,
    "title": "1984"
  }
]
➜  ~ curl http://localhost:5000/books/1

{
  "author": "TEST1",
  "id": 1,
  "title": "TEST1"
}
➜  ~ curl -X POST -H "Content-Type: application/json" \
-d '{"title": "Brave New World", "author": "Aldous Huxley"}' \
http://localhost:5000/books
{
  "author": "Aldous Huxley",
  "id": 3,
  "title": "Brave New World"
}

➜  ~ curl http://localhost:5000/books 

[
  {
    "author": "TEST1",
    "id": 1,
    "title": "TEST1"
  },
  {
    "author": "George Orwell",
    "id": 2,
    "title": "1984"
  },
  {
    "author": "Aldous Huxley",
    "id": 3,
    "title": "Brave New World"
  }
]
➜  ~ curl -X PUT -H "Content-Type: application/json" \
-d '{"title": "Updated Title", "author": "Updated Author"}' \
http://localhost:5000/books/1

{
  "author": "Updated Author",
  "id": 1,
  "title": "Updated Title"
}
➜  ~ curl http://localhost:5000/books                 

[
  {
    "author": "Updated Author",
    "id": 1,
    "title": "Updated Title"
  },
  {
    "author": "George Orwell",
    "id": 2,
    "title": "1984"
  },
  {
    "author": "Aldous Huxley",
    "id": 3,
    "title": "Brave New World"
  }
]

