#test.py

from app import app
from db_setup import init_db, db_session
from forms import PesquisaProduto, ProdutoForm
from flask import flash, render_template, request, redirect
from models import Produto
from tables import *

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
	#definicao da pagina inicial
	pesquisa = PesquisaProduto(request.form)
	if request.method == 'POST':
		return resultados_pesquisa(pesquisa)

	return render_template('index.html', form=pesquisa)

@app.route('/resultados')
def resultados_pesquisa(pesquisa):
	#Efetuar a pesquisa de um produto
	resultados = []
	search_string = pesquisa.data['search']

	if pesquisa.data['search'] == '':
		qry = db_session.query(Produto)
		results = qry.all()

	if not resultados:
		flash('Nenhum resultado encontrado')
		return redirect('/')

	else:
		#apresentar resultados
		table = Resultados(results)
		tabel.border = True
		return render_template('results.html', table=table)


@app.route('/novo_produto', methods=['GET', 'POST'])
def novo_produto():
	#Adicionar um novo produto
	form = ProdutoForm(request.form)
	
	if request.method == 'POST' and form.validate():
		#gravar os dados do novo produto
		produto = Produto()
		save_changes(produto, form, new=True)
		flash(' Novo produto criado com sucesso!')
		return redirect('/')

	return render_template('novo_produto.html', form=form)

def save_changes(produto, form, new=False):
	#gravar os dados do formulario na base de dados criada
	#utilizar os dados do formulario e atribuilos aos cmapos correspondentes da base de dados
	produto.nome = form.nome.data
	produto.preco = form.preco.data
	produto.quantidade = form.quantidade.data
	
	if new:
		#adiciona o novo produto a base de dados
		db_session.add(produto)
	db_session.commit()

if __name__ == '__main__':
	app.run()
