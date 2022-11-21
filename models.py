from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

DEFAULT_IMAGE_URL = "https://www.freeiconspng.com/uploads/name-people-person-user-icon--icon-search-engine-1.png"


# MODELS GO BELOW!
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    first_name = db.Column(db.String(20),
                     nullable=False,
                     unique=True)

    last_name = db.Column(db.String(20), 
                     nullable= False)

    image_url = db.Column(db.Text, nullable=False, default= DEFAULT_IMAGE_URL)
    posts = db.relationship('Post')

class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key = True, autoincrement =True)
    title = db.Column(db.String(40), nullable = False, unique = True)
    content = db.Column(db.Text, nullable = False, unique = False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    users = db.relationship('User')



   