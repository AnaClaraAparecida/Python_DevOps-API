import semana_1.flask as flask
import montydb

app = flask.Flask(__name__)

def get_conn(database):
    client = montydb.MontyClient()
    return client.get_database(database)

@app.route("/users/delete/<username>", methods=["DELETE"])
def delete_by_username(username):
    db = get_conn('pessoa')

    if db.users.count_documents({'username': username}) != 1:
        return flask.jsonify({'NOK': 'Usuário não encontrado'}), 400

    db.users.delete_one({'username': username})
    return flask.jsonify({'ACK': 'Usuário removido com sucesso'}), 200

@app.route("/users/update", methods=["PUT"])
def update_user():
    db = get_conn('pessoa')

    user = flask.request.json

    if db.users.count_documents({'username': user.get('username')}) != 1:
        return flask.jsonify({'NOK': 'Usuário não encontrado'}), 400

    db.users.update_one({'username': user.get('username')}, {"$set": user})
    return flask.jsonify({'ACK': 'Usuário atualizado com sucesso', 'data': user}), 200

@app.route("/users/insert", methods=["POST"])
def add_user():
    db = get_conn('pessoa')
    user = flask.request.json
    db.users.insert_one(user)
    return flask.jsonify({'ACK': 'Usuário inserido com sucesso', 'usuario': user}), 201

@app.route("/users", methods=["GET"])
def get_users():
    db = get_conn('pessoa')
    users = [
        {
            'username': user.get('username'),
            'senha': user.get('senha'),
            'nome': user.get('nome')
        } for user in db.users.find()
    ]
    return flask.jsonify(users), 200

@app.route("/users/<username>", methods=["GET"])
def get_users_by_username(username):
    db = get_conn('pessoa')
    users = [
        {
            'username': user.get('username'),
            'senha': user.get('senha'),
            'nome': user.get('nome')
        } for user in db.users.find({"username": username})
    ]
    return flask.jsonify(users), 200

@app.route("/", methods=["GET"])
def hello_from_flask():
    return flask.jsonify({'message': 'hello from flask'}), 200

@app.route("/outrarota", methods=["GET"])
def outra_funcionalidade():
    return flask.jsonify({'outra': 'mensagem'}), 200

if __name__ == '__main__':
    app.run(debug=True)
