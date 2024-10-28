from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # Import CORS to allow cross-origin requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and enable CORS
db = SQLAlchemy(app)
CORS(app)  # Allow React frontend to communicate with Flask API

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)

# Initialize the database with the application context
with app.app_context():
    db.create_all()

# Route to get all users in JSON format
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'name': user.name, 'surname': user.surname} for user in users]
    return jsonify(user_list)

# Route to create a new user via POST request
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    surname = data.get('surname')

    if not name or not surname:
        return jsonify({'error': 'Invalid input'}), 400

    new_user = User(name=name, surname=surname)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'id': new_user.id, 'name': new_user.name, 'surname': new_user.surname}), 201

# Route to update an existing user via PUT request
@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    data = request.get_json()

    user.name = data.get('name', user.name)
    user.surname = data.get('surname', user.surname)
    db.session.commit()

    return jsonify({'id': user.id, 'name': user.name, 'surname': user.surname})

# Route to delete a user
@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})

if __name__ == '__main__':
    app.run(debug=True)
