from datetime import date, timedelta

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from project import db
from project.models import User, Exercise
from project.main.forms import ExerciseForm

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("main/index.html")


@bp.route("/add_exercise", methods=["GET", "POST"])
@login_required
def add_exercise():
    form = ExerciseForm()
    if form.validate_on_submit():
        exercise = Exercise(
            exercise=form.exercise.data,
            calories=form.calories.data,
            timestamp=form.date.data,
            author=current_user
        )
        db.session.add(exercise)
        db.session.commit()
        flash("Great job partner! Make sure to come back tomorrow and GET SOME MORE!")
        return redirect(url_for("main.standings"))
    return render_template("main/add_exercise.html", form=form)


@bp.route("/standings")
@login_required
def standings():
    users = sorted(User.query.all(), key=lambda k: k.calories_burnt, reverse=True)
    standings = []

    for place, user in enumerate(users, start=1):
        standings.append(
            {"place": place, "name": user.name, "calories": user.calories_burnt}
        )

    exercises = sorted(Exercise.query.all(), key=lambda k: k.calories, reverse=True)[:3]
    top_exercises = []

    for place, exercise in enumerate(exercises, start=1):
        top_exercises.append(
            {"place": place,
             "name": User.query.get(exercise.user_id).name,
             "calories": exercise.calories,
             "exercise": exercise.exercise}
        )

    return render_template("main/standings.html", standings=standings,
                           top_exercises=top_exercises)


@bp.route("/history")
@login_required
def history():
    start_date = date(2019, 10, 1)
    delta = date.today() - start_date
    exercises = Exercise.query.all()
    data = []
    for day_index in range(delta.days + 1):
        day = start_date + timedelta(days=day_index)
        todays_exercises = []
        for exercise in exercises:
            if day == exercise.date:
                todays_exercises.append({
                    "author": exercise.author_name,
                    "exercise": exercise.exercise,
                    "calories": exercise.calories
                })
        data.append({
            "date": day,
            "exercises": todays_exercises
        })
    return render_template("main/history.html", data=data)
