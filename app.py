from flask import Flask, Blueprint, jsonify
from flask_restplus import Api
from ma import ma
from db import db

from resources.store import Store, StoreList, store_ns, stores_ns
from resources.item import Item, ItemList, items_ns, item_ns
from marshmallow import ValidationError

app = Flask(__name__)

# DB config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

# API + Blueprint
bluePrint = Blueprint('api', __name__, url_prefix='/api')
api = Api(bluePrint, doc='/doc', title='Sample Flask-RestPlus Application')
app.register_blueprint(bluePrint)

# ✅ init extensions AFTER app is created
db.init_app(app_
