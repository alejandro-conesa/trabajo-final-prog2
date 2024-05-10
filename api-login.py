from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import hashlib

app_users = Flask(__name__)
app_users.config['JWT_SECRET_KEY'] = 'easy_gest238973'
jwt = JWTManager(app_users)

users = {}
organizers = {}
assistants = {}
events = {}

# cargar y guardar datos en la BD
def load():
    pass

def save():
    pass

# funciones get, post, put y delete
@app_users.route('/data', methods=['GET'])
@jwt_required()

@app_users.route('/data', methods=['POST'])
@jwt_required()

@app_users.route('/data', methods=['PUT'])
@jwt_required()

@app_users.route('/data', methods=['DELETE'])
@jwt_required()

# funciones de registro/inicio de sesión
@app_users.route('/signup', methods=['POST'])
def signup():
    user = request.args.get('user', '')
    if user in users:
        return f'Usuario {user} ya existe', 409
    else:
        password = request.args.get('password', '')
        hashed = hashlib.sha256(password.encode()).hexdigest()
        users[user] = hashed
        return f'Usuario {user} registrado', 200


if __name__ == '__main__':
    app_users.run(debug=True)

