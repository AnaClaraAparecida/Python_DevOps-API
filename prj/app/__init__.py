from flask import Flask 
from .config.environment import ProductionEnvironment 

def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionEnvironment())

    return app
