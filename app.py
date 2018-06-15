#app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///servidor.db'
app.secret_key = "12345"

db = SQLAlchemy(app)
