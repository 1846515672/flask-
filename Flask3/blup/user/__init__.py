from flask import Blueprint

user = Blueprint("user", __name__)

from blup.user import views