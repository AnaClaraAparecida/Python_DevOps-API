import flask
import montydb

app = flask.Flask(__name__)

def get_conn(database):
    client = montydb.MontyClient()
    return client.get_database(database)

# ---------------- ROTAS ---------------- #

# Deletar usuário pelo username
@app.route("/users/delete/<username>", methods=["DELETE"])
def delete_by_username(username):
    db = get_conn("pessoa")

    result = db.users.delete_one({"username": username})
    if result.deleted_count == 0:
        return flask.jsonify({"NOK": "Usuário não encontrado"}), 404

    return flask.jsonify({"ACK": "Usuário removido com sucesso"}), 200


# Inserir novo usuário
@app.route("/users/insert", methods=["POST"])
def add_user():
    db = get_conn("pessoa")
    user = flask.request.json

    if not user or "username" not in user or "senha" not in user or "nome" not in user:
        return flask.jsonify({"NOK": "Campos obrigatórios: username, senha, nome"}), 400

    if db.users.find_one({"username": user["username"]}):
        return flask.jsonify({"NOK": "Usuário já existe"}), 400

    db.users.insert_one(user)
    return flask.jsonify({"ACK": "Usuário inserido com sucesso", "usuario": user}), 201


# Listar todos os usuários
@app.route("/users", methods=["GET"])
def get_users():
    db = get_conn("pessoa")

    users = [
        {
            "username": user.get("username"),
            "senha": user.get("senha"),
            "nome": user.get("nome"),
        }
        for user in db.users.find()
    ]
    return flask.jsonify(users), 200


# Buscar usuário pelo username
@app.route("/users/<username>", methods=["GET"])
def get_user_by_username(username):
    db = get_conn("pessoa")

    user = db.users.find_one({"username": username})
    if not user:
        return flask.jsonify({"NOK": "Usuário não encontrado"}), 404

    return flask.jsonify(
        {
            "username": user.get("username"),
            "senha": user.get("senha"),
            "nome": user.get("nome"),
        }
    ), 200


# Rota principal
@app.route("/", methods=["GET"])
def hello_from_flask():
    return flask.jsonify({"message": "hello from flask"}), 200


# Outra rota de exemplo
@app.route("/outrarota", methods=["GET"])
def outra_funcionalidade():
    return flask.jsonify({"outra": "mensagem"}), 200


# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    app.run(port=5000, debug=True)
