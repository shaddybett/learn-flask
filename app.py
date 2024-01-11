from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from models import Book,Author

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learn.db'
db = SQLAlchemy(app)

@app.route('/')
def home():
    return 'Welcome home!'

@app.route('/books')
def books():
    books_list= Book.query_all()
    return render_template('books.html', books=books_list)

@app.route('/authors')
def authors():
    authors_list = Author.query_all()
    return render_template('authors.html',authors=authors_list)   

if __name__=='__main__':
    app.run(debug=True)
