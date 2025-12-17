from flask import Blueprint, current_app, jsonify 

blueprint = Blueprint("hello", __name__)

@blueprint.route("/hello")
def hello():
    current_app.logger.info(f'{__name__}: Estou na blueprint')
    return jsonify({
        'message': 'teste de log em blueprints.'

    })
