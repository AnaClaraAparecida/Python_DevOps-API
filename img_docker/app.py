from flask import Flask, jsonify 

app = Flask(__name__)

@app.route("/")
def get_index():
    return jsonify({'mensagem':'hello from flask inside a container'})
