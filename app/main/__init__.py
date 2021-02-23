from flask import Blueprint
main = Blueprint('main',__name__)
from . import views, error
#initialize blueprint class


def create_app(config_name):
    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    #Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # #setting config
    # configer_request(app)

    #will add the viewss and forms
    return app