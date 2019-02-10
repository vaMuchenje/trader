
from flask import Flask
import mimetypes
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


mimetypes.add_type('image/svg+xml', '.svg')

app= Flask(__name__)
app.config.from_object(Config)
db= SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
from app import routes, models
