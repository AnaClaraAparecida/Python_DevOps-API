from flask import Flask 
from app.config.environment import ProductionEnvironment 
from app.routes.index import blueprint as index 

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionEnvironment())
    # definir paramentro de config 

    app.register_blueprint(index)
    # colocar as demais blueprints 

    return app

