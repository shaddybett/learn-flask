# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
# from models import db, Book, Author

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learn.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

# # Create the database tables
# # with app.app_context():
# #     db.create_all()

# @app.route('/')
# def home():
#     return 'Welcome home!'

# @app.route('/books')
# def books():
#     books_list = Book.query.all()
#     return render_template('books.html', books=books_list)

# @app.route('/authors')
# def authors():
#     authors_list = Author.query.all()
#     return render_template('authors.html', authors=authors_list)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from models import db,Book,Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///best.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return 'HEllo and welcome'

@app.route('/books')
def books():
    books_list = Book.query.all()
    return render_template('books.html',books = books_list)

@app.route('/authors')
def authors():
    authors_list = Author.query.all()
    return render_template('authors.html',authors = authors_list)

if __name__=='__main__':
    app.run(debug=True)