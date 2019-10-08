from flask import redirect, url_for, flash, request, render_template
from flask_login import current_user, login_user, logout_user
from werkzeug.urls import url_parse
from project import db
from project.models import User
from project.auth import bp
from project.auth.forms import LoginForm, RegistrationForm


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.add_exercise"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password")
            return redirect(url_for("auth.login"))
        login_user(user)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("main.add_exercise")
        return redirect(next_page)
    return render_template("auth/login.html", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@bp.route("/registration", methods=["GET", "POST"])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('main.add_exercise'))
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
        return redirect(url_for("auth.login"))
    return render_template("auth/registration.html", form=form)
