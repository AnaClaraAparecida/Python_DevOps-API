from flask import Blueprint, jsonify
from blueprint.database import get_conn
import montydb

def get_conn(database):
    client = montydb.MontyClient()
    return client.get_database(database )

blueprint = Blueprint("users", __name__)

@blueprint.route("/users", methods=["GET"])
def get_users():
    db = get_conn('pessoa')  # depende de como você configurou get_conn
    users = [
        {
            'username': user.get('username'),
            'senha': user.get('senha'),
            'nome': user.get('nome')
        }
        for user in db.users.find()
    ]
    return jsonify(users), 200
