from flaskmain import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(16), nullable=False, unique=False)
    password_hash = db.Column(db.String(256))

    @property
    def password(self):
        raise Exception("密码无法查看")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Article(db.Model):
    __tablename__ = 't_article'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(16))
    content = db.Column(db.Text)
