from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config['SECRET_KEY'] = '26c2bff84d8e9ac87bb08dc1' 
db = SQLAlchemy(app)

from market import routes
