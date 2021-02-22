from flask import Flask
from flask-bootstrap import Bootstrap

bootstrap = Bootstrap()

def create app(config_name):
    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])