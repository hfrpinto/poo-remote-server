#forms.py

from wtforms import Form, StringField, SelectField

class PesquisaProduto(Form):
	opcoes = [('Produto', 'Produto')]
	select = SelectField('Pesquisar por:', choices=opcoes)
	search = StringField('')

class ProdutoForm(Form):
	nome = StringField('nome')
	preco = StringField('preco')
	quantidade = StringField('quantidade')
