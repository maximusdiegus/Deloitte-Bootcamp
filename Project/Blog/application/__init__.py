from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('mysecretkey')

db = SQLAlchemy(app)

from application import routes