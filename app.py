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

# init extensions
db.init_app(app)
ma.init_app(app)

# ✅ צור את הטבלאות מיד כשעולה האפליקציה (לא דרך before_first_request)
with app.app_context():
    db.create_all()

# Namespaces
api.add_namespace(item_ns)
api.add_namespace(items_ns)
api.add_namespace(store_ns)
api.add_namespace(stores_ns)

@api.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(error.messages), 400

# Routes
item_ns.add_resource(Item, '/<int:id>')
items_ns.add_resource(ItemList, "")
store_ns.add_resource(Store, '/<int:id>')
stores_ns.add_resource(StoreList, "")

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')
