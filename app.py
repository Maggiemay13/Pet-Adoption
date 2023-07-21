from flask import Flask, render_template, redirect, session, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)


with app.app_context():
    db.create_all()


@app.route("/")
def home_page():
    """Render home page"""
    pets = Pet.query.all()
    return render_template("home_pet_list.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Add a pet"""

    form = AddPetForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        species = form.species.data

        new_pet = Pet(name=name, age=age, species=species)
        db.session.add(new_pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("pet_add_form.html", form=form)


@app.route("/<int:pet_id>", methods=["GET", "POST"])
def edit_pet(pet_id):
    """Edit pet form"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.available = form.available.data
        pet.photo_url = form.photo_url.data
        db.session.commit()
        return redirect(url_for('home_page'))
    else:
        return render_template("pet_edit_form.html", form=form, pet=pet)
