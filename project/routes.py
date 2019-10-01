from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from project import app, db
from project.forms import LoginForm, ExerciseForm, RegistrationForm
from project.models import User, Exercise


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
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
        return redirect(url_for("index"))
    return render_template("index.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password")
            return redirect(url_for("login"))
        login_user(user)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/standings")
@login_required
def standings():
    users = User.query.all()
    standings = []
    for user in users:
        standings.append({"name": user.name, "calories": user.calories_burnt})
    standings = sorted(standings, key=lambda k: k["calories"], reverse=True)
    return render_template("standings.html", standings=standings)


@app.route("/registration", methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            email=form.email.data,
            password=form.password.data
        )
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you have registered for Sober October challenge!")
        return redirect(url_for("login"))
    return render_template("registration.html", form=form)
