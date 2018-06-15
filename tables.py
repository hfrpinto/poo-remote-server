#tables.py

from flask_table import Table, Col

class Resultados(Table):
	id = Col('ID', show=False)
	nome = ('nome')
	preco = ('preco')
	quantidade = ('quantidade')

