from flask import Blueprint

chane_bp = Blueprint('chane', __name__, template_folder='templates')

from . import views
