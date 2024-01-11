import app
from app import db, Book,Author

book_data = {
    'name': 'All Over',
    'author': 'Yavus',
    'Pages': 200
}

author_data = {
    'name' : 'Shakesphere',
    'age': 28,
    'book': 'R&Juliette'
}

with app.app_context():
    new_book = Book(**book_data)
    new_author = Author(**author_data)

    db.session.add(new_book)
    db.session.add(new_author)
    db.session.commit()