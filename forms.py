from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange, URL, Length


class AddPetForm(FlaskForm):
    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[
                          ("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[
                       Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes")
    avaiable = BooleanField("Is this Pet Avaiable?")


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")
