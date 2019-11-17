from flask_sqlalchemy import SQLAlchemy
from flask import Flask



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings.DebugConfig")

    db.init_app(app)

    from blup.course import course
    from blup.user import user

    app.register_blueprint(course, url_prefix="/course/")
    app.register_blueprint(user, url_prefix="/user/")

    return app