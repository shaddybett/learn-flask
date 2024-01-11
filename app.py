from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learn.db'
db = SQLAlchemy(app)
@app.route('/')
def home():
    return 'Welcome home!'

if __name__=='__main__':
    app.run(debug=True)
