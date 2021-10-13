from flask import Flask
from models import db
from config import Config
from views import views


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(views, url_prefix='')



if __name__ == '__main__':
    app.run()
