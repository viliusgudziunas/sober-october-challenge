from datetime import date, timedelta
from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from project import db
from project.models import User, Exercise
from project.main import bp
from project.main.forms import ExerciseForm


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
            date=form.date.data,
            author=current_user
        )
        db.session.add(exercise)
        db.session.commit()
        flash("Exercise submitted!")
        return redirect(url_for("main.standings"))
    return render_template("main/add_exercise.html", form=form)


@bp.route("/standings")
@login_required
def standings():
    users = sorted(
        User.query.all(), key=lambda k: k.calories_burnt, reverse=True
    )
    standings = []
    place = 1
    for user in users:
        standings.append({
            "place": place,
            "name": user.name,
            "calories": user.calories_burnt
        })
        place += 1
    return render_template("main/standings.html", standings=standings)


@bp.route("/history")
@login_required
def history():
    start_date = date(2019, 10, 1)
    delta = date.today() - start_date
    dates_in_october = []
    for day in range(delta.days + 1):
        dates_in_october.append(start_date + timedelta(days=day))
    exercises = Exercise.query.all()
    return render_template("main/history.html", dates=dates_in_october, exercises=exercises)
