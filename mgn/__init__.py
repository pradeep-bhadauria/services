import os
import sys
from config import _basedir

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

mgn = Flask(__name__)

mgn.config.from_object('config')

db = SQLAlchemy(mgn)

@mgn.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()

# Module user
from mgn.user.views import mod as usersModule
mgn.register_blueprint(usersModule)
