#db_creator.py - criador da base de dados

from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///servidor.db', echo=True) # definicaoda engine para a criacao da base de dados e o nome a dar a base de dados a ser criada.
Base = declarative_base()

class Produto(Base):
	__tablename__ = "produtos" #definicao do nome a atribuir a tabela dentro da base de dados

	id = Column(Integer, primary_key=True)
	nome = Column(String)
	preco = Column(String)
	quantidade = Column(String)
	#definicao das diferentes colunas de preenchimento da base de dados, com o nome, preco e quantidade do produto.

	
Base.metadata.create_all(engine) 
