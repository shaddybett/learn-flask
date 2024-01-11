
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Book(db.Model):
    __tablename__='books'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable = False)
    author = db.Column(db.String(200),nullable = False)
    pages = db.Column(db.Integer)

class Author(db.Model):
    __tablename__='authors'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable = False) 
    age = db.Column(db.Integer,nullable = False)
    book = db.Column(db.String(200))   
