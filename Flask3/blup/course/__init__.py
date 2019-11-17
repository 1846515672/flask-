from flask import Blueprint

course = Blueprint("course", __name__)

from blup.course import views