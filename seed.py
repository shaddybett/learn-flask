# from models import db, Book, Author
# from flask import Flask

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learn.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

# # Create the application context
# with app.app_context():
#     book_data = {
#         'name': 'All Over',
#         'author': 'Yavus',
#         'pages': 200
#     }

#     author_data = {
#         'name': 'Shakespeare',
#         'age': 28,
#         'book': 'R&Juliette'
#     }

#     # Add the data to the database
#     new_book = Book(**book_data)
#     new_author = Author(**author_data)

#     # Use the database session to add and commit the data
#     with db.session.begin():
#         db.session.add(new_book)
#         db.session.add(new_author)
from flask import Flask

from models import db,Book,Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///best.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    book_data={
        'title': 'goat',
        'author': 'Kai',
        'pages': 100
    }
    author_data = {
        'name':'Chalo',
        'age': 20,
        'book': 'goat'
    }

    new_book = Book(**book_data)
    new_author = Author(**author_data)

    with db.session.begin():
        db.session.add(new_book)
        db.session.add(new_author)