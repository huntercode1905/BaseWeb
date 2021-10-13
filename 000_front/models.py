from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(32), nullable=True)
    content = db.Column(db.Text)
