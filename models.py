# -*- coding: UTF-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/phipolis.db'
app.secret_key = 'development key'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class Usuario(db.Model):
    __tablename__ = 'usuario'
    
    id_ = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String)
    nome = db.Column(db.String, unique = True)
    cpf = db.Column(db.String, unique = True)
    rg = db.Column(db.String, unique = True)
    endereco = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique = True)
    telefone = db.Column(db.String, unique = True)
    admin = db.Column(db.Boolean, default=False)
		

    def __init__(self, username, password, nome, cpf, rg, endereco, email, telefone, admin):
        self.username   = username
        self.nome   = nome
        self.password   = password
        self.cpf     = cpf
        self.rg      = rg
        self.endereco      = endereco
        self.email      = email
        self.telefone     = telefone
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id_)

    def __repr__(self):
        return "<Usuario(username='%s', password='%s')>" % (self.username, self.password)





class Administrador(db.Model):
    __tablename__ = 'administrador'

    id_admin = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, db.ForeignKey('usuario.username'))

    usuario = db.relationship("Usuario", backref=db.backref('administradores'))

    def __init__(self, id_admin, username):
        self.id_admin   = id_admin
        self.username      = username
    
    def __repr__(self):
        return "<Administrador(administrador='%s')>" % (self.answer)


class Cliente(db.Model):
    __tablename__ = 'cliente'

    conta = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, nullable=False)
    sensor = db.Column(db.Integer, nullable=True)
    cota = db.Column(db.Integer) 
    username = db.Column(db.String, db.ForeignKey('usuario.username'))
    
    usuario = db.relationship("Usuario", backref=db.backref('clientes'))

    def __init__(self, status, sensor, cota, username):
        self.status   = status
        self.sensor        = sensor
        self.cota        = cota
        self.username        = username
    
    def __repr__(self):
        return "<Cliente(conta='%s', username='%r')>" % (self.conta, self.username)

class Consumo(db.Model):
    __tablename__ = 'consumo'

    id_consumo = db.Column(db.Integer, primary_key=True)
    conta = db.Column(db.Integer, db.ForeignKey('cliente.conta'))
    username = db.Column(db.Integer, db.ForeignKey('cliente.username'))
    mes = db.Column(db.String, nullable=False)
    ano = db.Column(db.Integer, default=False)
    valor = db.Column(db.Float, default=False)

    #usuario = db.relationship("Usuario", backref=db.backref('consumo'))
    #conta = db.relationship("Conta", backref=db.backref('consumo'))
    
    db.ForeignKeyConstraint(['conta', 'username'], ['cliente.conta', 'cliente.username'])

    def __init__(self, conta, username, mes, ano, valor):
        self.conta   = conta
        self.username    = username      
        self.mes = mes
        self.ano = ano
        self.valor = valor

    def __repr__(self):
        return "<Consumo(usuario='%s', conta='%r')>" % (self.username, self.conta)

class Contato(db.Model):
    __tablename__ = 'contato'

    id_contato = db.Column(db.Integer, primary_key=True)
    conta = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, primary_key=True)
    data = db.Column(db.Date)


    db.ForeignKeyConstraint(['conta', 'username'], ['cliente.conta', 'cliente.username'])

    def __init__(self, conta, username, data):
        self.conta   			 = conta
        self.username    = username
        self.data 				 = data
        
    def __repr__(self):
        return "<Conta(conta='%s', username='%r', data='%r')>" % (self.conta,\
         self.username, self.data)

class Fatura(db.Model):
    __tablename__ = 'fatura'
  
    id_fatura = db.Column(db.Integer, primary_key=True)
    valor  = db.Column(db.Float)
    data = db.Column(db.Date)
  
    def __init__(self, id_fatura, valor, data):
        self.id_fatura = id_fatura
        self.valor = valor
        self.data = data
        
    def __repr__(self):
        return "<"
    
      
      
class Pagamento(db.Model):
    __tablename__ = 'pagamento'
  
    id_pagamento = db.Column(db.Integer, primary_key=True)
    conta = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Integer, primary_key=True)
    id_fatura = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Date)
    
    db.ForeignKeyConstraint(['conta', 'username', 'id_fatura'],['cliente.conta', 'usuario.username', 'fatura.id_fatura'])
    
    def __init__(self, id_pagamento, conta, username, id_fatura, data):
        self.id_pagamento = id_pagamento
        self.conta = conta
        self.username = username
        self.id_fatura = id_fatura
        self.data = data
                                                               
    def __repr__(self):
        return "<"
                                                               
class Recibo(db.Model):
	__tablename__ = 'recibo'
	
	id_recibo = db.Column(db.Integer, primary_key=True)
	conta = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Integer, primary_key=True)
	id_pagamento = db.Column(db.Integer, primary_key=True)
	id_fatura = db.Column(db.Integer, primary_key=True)
	data_pagamento = db.Column(db.Date)
	valor = db.Column(db.Float)
	
	db.ForeignKeyConstraint(['conta', 'username', 'id_pagamento', 'id_fatura'], ['cliente.conta', 'usuario.username', 'pagamento.id_pagamento', 'fatura.id_fatura'])
	
	
	def __init__(self, id_recibo, conta, username, id_pagamento, id_fatura, data_pagamento, valor):
	    self.id_recibo = id_recibo
	    self.conta = conta
	    self.username = username
	    self.id_pagamento = id_pagamento
	    self.id_fatura = id_fatura
	    self.data_pagamento = data_pagamento
	    self.valor = valor
			
	def __repr__(self):
		return "<"
      
class Resposta(db.Model):
	__tablename__ = 'resposta'
	
	id_resposta = db.Column(db.Integer, primary_key=True)
	id_admin = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date)
	
	db.ForeignKeyConstraint(['id_admin', 'username'], ['administrador.id_admin', 'administrador.username'])
	
	
	def __init__(self, id_admin, username, date):
	    self.id_admin = id_admin
	    self.username = username
	    self.date = date
    
	def __repr__(self):
		return "<"


class Mensagem(db.Model):
	__tablename__ = 'mensagem'
	
	id_mensagem = db.Column(db.Integer, primary_key=True)
	id_contato = db.Column(db.Integer, primary_key=True)
	conta = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String, primary_key=True)
	id_resposta = db.Column(db.Integer, primary_key=True)
	id_admin = db.Column(db.Integer, primary_key=True)
	assunto = db.Column(db.String)
	conteudo = db.Column(db.String) 
	resposta = db.Column(db.String)
	status = db.Column(db.String)
	data_criacao = db.Column(db.Date)


	db.ForeignKeyConstraint(['conta', 'id_contato', 'username'], ['contato.conta', 'contato.id_contato', 'contato.username'])
	db.ForeignKeyConstraint(['id_resposta', 'id_admin', 'username'], ['resposta.id_resposta', 'resposta.id_admin', 'resposta.username'])
	
	def __init__(self, id_contato, conta, username, id_resposta, id_admin, assunto, conteudo, resposta, status, data_criacao):
			self.id_contato = id_contato
			self.id_resposta = id_resposta
			self.id_admin = id_admin
			self.assunto = assunto
			self.conteudo = conteudo
			self.resposta = resposta
			self.conta = conta
			self.username = username
			self.data_criacao = data_criacao
			self.status = status

	def __repr__(self):
		return "<"

db.create_all()

if Usuario.query.filter_by(username='admin', password='admin').first():
    pass
else:
    admin = Usuario('admin', 'admin', 'fulano', 1234, 1234, 'ufpa guama', 'oitdb@hotmail.com', '12312', 1)
    db.session.add(admin)
    db.session.commit()

