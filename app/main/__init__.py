from flask import Blueprint
from . import views, error
#initialize blueprint class

main = Blueprint('main',__name__)
