from flask import Flask, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import hashlib

app_users = Flask(__name__)
app_users.config['JWT_SECRET_KEY'] = 'easy_gest238973'
jwt = JWTManager(app_users)

users = {}
data = {}

def load():
    pass

def save():
    pass

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

