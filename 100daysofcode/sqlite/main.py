from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"

db.app = app
db.init_app(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String, unique=True, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)


book = Books(
    id = 0,
    title = "Klara und die Sonne",
    author = "Kazuo Ishiguro",
    rating = "5",
)

with app.app_context():
    db.session.add(book)
    db.session.commit()



