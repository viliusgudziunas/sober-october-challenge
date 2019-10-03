from datetime import datetime
from flask import current_app
from flask_login import UserMixin
from project import db, bcrypt, login


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    exercises = db.relationship("Exercise", backref="author", lazy="dynamic")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, current_app.config.get("BCRYPT_LOG_ROUNDS")
        ).decode()

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @property
    def calories_burnt(self):
        exercises = Exercise.query.filter(Exercise.user_id == self.id).all()
        calories = 0
        for exercise in exercises:
            calories += exercise.calories
        return calories


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Exercise(db.Model):
    __tablename__ = "exercises"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exercise = db.Column(db.String(64), nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    def __init__(self, exercise, calories, date, author):
        self.exercise = exercise
        self.calories = calories
        self.date = date
        self.user_id = author.id
