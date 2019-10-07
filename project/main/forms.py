from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, SubmitField
from wtforms.validators import DataRequired, ValidationError


class ExerciseForm(FlaskForm):
    exercise = StringField("Exercise", validators=[DataRequired()])
    calories = IntegerField("Calories Burnt", validators=[DataRequired()])
    date = DateField(
        "Date", format="%d/%m/%y", default=datetime.today, validators=[DataRequired()]
    )
    submit = SubmitField("Add")

    def validate_calories(self, calories):
        if not calories.data > 0:
            raise ValidationError(
                "Cannot enter a negative amount of calories."
            )

    def validate_date(self, date):
        start = datetime(2019, 10, 1)
        if datetime.now() < datetime(2019, 11, 1):
            end = datetime.now()
        else:
            end = datetime(2019, 11, 1)
        given_date = datetime(date.data.year, date.data.month, date.data.day)
        if not start <= given_date < end:
            raise ValidationError(
                "Date must be between the 1st of October and today."
            )
