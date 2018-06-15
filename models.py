#models.py

from app import db

class Produto(db.Model):
	__tablename__ = "produtos"

	id = db.Column(db.Integer, primary_key=True)
	nome = db.Column(db.String)
	preco = db.Column(db.String)
	quantidade = db.Column(db.String)
