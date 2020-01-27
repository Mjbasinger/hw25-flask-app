#import necessary items for app. g is for global access throughout app
from flask import Flask, jsonify, g
from flask_login import LoginManager
from flask_cors import CORS
app = Flask(__name__)
#imoports models and resources
import models
from resources.animals import animals
login_manager = LoginManager()
login_manager.init_app(app)

import models
from resources.animals import animals
from resources.users import users

CORS(animals, origin=['http://localhost:3000'], supports_credentials=True)
CORS(users, origin=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(animals, url_prefix='/api/v1/animals')
app.register_blueprint(users, url_prefix='/api/v1/users')
# this is the logic for connection and close. First connect before each request, then close
@app.before_request
def before_request():
    g.db = models.DATABASE
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.route('/')
def index():
    return 'test'

DEBUG = True
PORT = 8000
if __name__ == '__main__':
    models.initialize()
    app.run(debug=DEBUG, port=PORT)