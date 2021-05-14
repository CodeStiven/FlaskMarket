from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app: Flask = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config["SECRET_KEY"] = "26c2bff84d8e9ac87bb08dc1"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
