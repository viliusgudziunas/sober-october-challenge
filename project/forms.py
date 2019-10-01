from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from project.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")


class ExerciseForm(FlaskForm):
    exercise = StringField("Exercise", validators=[DataRequired()])
    calories = IntegerField("Calories Burnt", validators=[DataRequired()])
    date = DateField(
        "Date", format="%d/%m/%y", default=datetime.today, validators=[DataRequired()]
    )
    submit = SubmitField("Add")

    def validate_date(self, date):
        start = datetime(2019, 10, 1)
        end = datetime(2019, 11, 1)
        given_date = datetime(date.data.year, date.data.month, date.data.day)
        if not start <= given_date < end:
            raise ValidationError("Date must be in October.")


class RegistrationForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField(
        "Repeat Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        valid_emails = [
            "vilius@email.com",
            "titas@email.com",
            "marius@email.com"
        ]
        if user is not None or email.data not in valid_emails:
            raise ValidationError("Please use a different email address.")