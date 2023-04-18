from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, URLField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

class AddPetForm(FlaskForm):
  name = StringField("Name", validators=[InputRequired()])
  species = StringField("Species", validators=[InputRequired(), AnyOf(values=["Dog", "Cat", "Porcupine", "dog", "cat", "porcupine"], message="Only cats, dogs, or porcupines are accepted.")])
  photo = URLField("Photo url", validators=[Optional(strip_whitespace=True), URL()])
  age = IntegerField("Age", validators=[NumberRange(min=1, max=29)])
  notes = StringField("Notes", validators=[Optional(strip_whitespace=True)])
  available = BooleanField("Available", default=True)
  
class EditPetForm(FlaskForm):
  name = StringField("Name", render_kw={'readonly': True})
  species = StringField("Species", render_kw={'readonly': True})
  age = IntegerField("Age", render_kw={'readonly': True})
  photo = URLField("Photo url (edit)", validators=[Optional(strip_whitespace=True)])
  notes = StringField("Notes (edit)", validators=[Optional(strip_whitespace=True)])
  available = BooleanField("Available (edit)", default=True)
  