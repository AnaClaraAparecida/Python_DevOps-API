from Flask import Blueprint, jsonify
from config.database import get_conn

blueprint = Blueprint("users", ["GET"])

@blueprint.route("/users", methods=["GET"])
def get_users():
    db = get_conn('pessoa')

    users = [
        {
            'username': user.get('username'), 
            'senha': user.get('senha'),
            'nome': user.get('nome')
        } for user in db.users.find()
    ]
    return flask.jsonify(users)

