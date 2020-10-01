from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from project.models import User


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign In")


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
            "marius@email.com",
            "ainis@email.com",
            "aleksandras@email.com",
            "arnas@email.com",
            "aurimas@email.com",
            "deimante@email.com",
            "dominykas@email.com",
            "gintare@email.com",
            "izabele@email.com",
            "martynas@email.com",
            "olivija@email.com",
            "titas@email.com",
            "vilius@email.com"
        ]
        if user is not None or email.data not in valid_emails:
            raise ValidationError("Please use a different email address.")
