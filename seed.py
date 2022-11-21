"""Seed file to make sample data for users db. We will
execute this seed.py before we run app.py"""

from models import User, db, Post
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

post1 = Post(title='First post', content = "I love my day", users = user1)
post2 = Post(title='Yet Another Post', content = "I love my family", users = user2)
post3 = Post(title='Flask Is Awesome', content = "I learn Flask everyday", users = user3)


# Add new objects to session, so they'll persist
db.session.add_all([user1, user2, user3, post1, post2, post3])

# Commit--otherwise, this never gets saved!
db.session.commit()
