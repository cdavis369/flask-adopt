from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

with app.app_context():
  connect_db(app)
  db.create_all()
  
@app.route('/')
def homepage():
  pets = Pet.query.order_by(Pet.name)
  return render_template("index.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def new_pet_form():
  """ New pet form. """
  form = AddPetForm()
  if form.validate_on_submit():
    name = form.name.data
    species = form.species.data
    photo = form.photo.data
    age = form.age.data
    notes = form.notes.data
    available = form.available.data
    pet = Pet(name=name, species=species, photo=photo, age=age, notes=notes, available=available)
    db.session.add(pet)
    db.session.commit()
    return redirect("/")
  else:
    return render_template("add_pet.html", form=form)

@app.route('/<int:id>', methods=["GET", "POST"])
def display_and_edit_pet(id):
  """ Edit Pet Form. Fills in form with pet details. """
  pet = Pet.query.get(id)
  form = EditPetForm(obj=pet)
  
  if form.validate_on_submit():
    pet.photo = form.photo.data
    pet.notes = form.notes.data
    pet.available = form.available.data
    db.session.commit()
    return redirect('/')
  
  return render_template("display_edit_pet.html", form=form, pet=pet)
    

@app.route("/delete/<int:id>")
def delete_pet(id):
  """ Delete pet. """
  Pet.query.filter_by(id=id).delete()
  db.session.commit()
  return redirect('/')