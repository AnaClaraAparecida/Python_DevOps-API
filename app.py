from flask import Flask, jsonify 
from os import getenv

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def get_index():
    return jsonify(
            {
                'message' : 'Hello from Heroku'
            }
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=getenv("PORT"))
