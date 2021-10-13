from flask import Flask
from flask_sqlalchemy import SQLAlchemy



class Config(object):
    DEBUG = True
    SECRET_KEY = "12434566HGFDSD*&^%"


db = SQLAlchemy()

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.Text, nullable=False)




app = Flask(__name__)


app.config.from_object(Config)


@app.route("/")
def index():
    return "Hello Flask"



if __name__ == '__main__':
    app.run()
