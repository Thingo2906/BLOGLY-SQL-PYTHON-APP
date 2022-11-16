"""Seed file to make sample data for users db. We will
execute this seed.py before we run app.py"""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
user1 = User(first_name='Tom', last_name="Brady")
user2 = User(first_name='John', last_name="Smith")
user3 = User(first_name='Sandy', last_name="Duncan")

# Add new objects to session, so they'll persist
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

# Commit--otherwise, this never gets saved!
db.session.commit()
