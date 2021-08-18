"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake
from forms import NewCupcakeForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)


@app.route('/')
def index():
    """Home page"""
    cupcakes = Cupcake.query.all()
    form = NewCupcakeForm()
    return render_template('index.html', cupcakes=cupcakes, form=form)


@app.route('/api/cupcakes/search')
def search_cupcakes():
    """Search for specific cupcakes"""
    search_term = request.args.get('search')
    cupcakes = Cupcake.query.filter(Cupcake.flavor.ilike(f'%{search_term}%'))
    form = NewCupcakeForm()
    return render_template('index.html', cupcakes=cupcakes, form=form)


@app.route('/api/cupcakes')
def get_all_cupcakes():
    """Returns all cupcakes"""
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def get_cupcake_info(id):
    """Returns data about a single cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    """Creates a Cupcake"""
    new_cupcake = Cupcake(flavor=request.json['flavor'], size=request.json['size'],
                          rating=request.json['rating'], image=request.json.get('image', 'https://tinyurl.com/demo-cupcake'))
    db.session.add(new_cupcake)
    db.session.commit()
    response_json = jsonify(cupcake=new_cupcake.serialize())
    return (response_json, 201)


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def edit_cupcake(id):
    """Updates Cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    """Deletes cupcake"""
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='Deleted')
