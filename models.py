
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.integer,primary_key=True)
    name = db.Column(db.string(200),nullable = False)
    author = db.Column(db.string(200),nullable = False,foreignKey = 'author')
    pages = db.Column(db.integer(4))

class Author(db.Model):
    __tablename__='authors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.string(200),nullable = False) 
    age = db.Column(db.integer(4),nullable = False)
    book = db.Column(db.string(200))   
