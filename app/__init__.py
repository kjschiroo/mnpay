from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import yaml


# Load in yml configs
with open('database.yml', 'r') as f:
    config = yaml.load(f)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['production']['uri']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

CORS(app)

from app import models, controllers
