from flask import Flask
from flask-bootstrap import Bootstrap

bootstrap = Bootstrap()

def create app(config_name):
    app = Flask(__name__)

    #Creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    #Registering the blueprint
    from.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #setting config
    from.request import configer_request
    configer_request(app)

    #will add the viewss and forms
    return app
    