# -*- coding: UTF-8 -*-

from flask import request, redirect, url_for, \
             render_template, flash
from flask_login import login_user ,logout_user, login_required, current_user
from models import db, app, login_manager, Usuario, Administrador, Cliente, Consumo, \
 Fatura, Pagamento, Recibo, Resposta, Mensagem
import os
import subprocess
from collections import Counter
from sqlalchemy.sql.expression import update


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        registered_user = Usuario.query.filter_by(username=username,password=password).first()
        if registered_user:
            login_user(registered_user)
            if registered_user.admin == 1:
	            return redirect(url_for('admin'))
            else:
							return redirect(url_for('cliente'))
        error = 'Username or Password is invalid or User is disabled'
    return render_template('index.html', error=error)

@app.route('/cadastro', methods=['GET','POST'])
def cadastro():
    register = True
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['senha']
        nome = request.form['nome']
        rg = request.form['rg']
        telefone = request.form['telefone']
        cpf = request.form['cpf']
        email = request.form['email']
        endereco = request.form['endereco']
        add_user = Usuario(username, nome, password, cpf, rg, endereco, email, telefone)
        db.session.add(add_user)
        db.session.commit()
        flash('You were registered')
    return render_template('cadastro.html', register=register)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You were logged out')
    return redirect(url_for('login'))

@app.route('/admin', methods=['GET'])
@login_required
def admin():
    chamadas_aberto = Mensagem.query.filter(Mensagem.status == 'aberto').all()
    chamadas_fechado = Mensagem.query.filter(Mensagem.status == 'fechado').all()
    chamadas_em_atendimento = Mensagem.query.filter(Mensagem.status == 'em_atendimento').all()
    chamadas = Mensagem.query.all()
    return render_template('areaAdmin.html', aberto=len(chamadas_aberto), fechado=len(chamadas_fechado),\
 atendimento=len(chamadas_em_atendimento), todas=chamadas)

@app.route('/cliente', methods=['GET'])
@login_required
def cliente():
		#pegar aqui os dados de consumo do banco
    consumo = Consumo.query.filter(Consumo == 'aberto').all()
    chamadas_fechado = Mensagem.query.filter(Mensagem.status == 'fechado').all()
    chamadas_aberto = Mensagem.query.filter(Mensagem.status == 'aberto').all()
    chamadas = Mensagem.query.all()
    return render_template('areaCliente.html', aberto=len(chamadas_aberto), fechado=len(chamadas_fechado), todas=len(chamadas))

@app.route('/reclamacoes', methods=['GET','POST'])
@login_required
def reclamacoes():
		error = None
		if request.method == 'POST':
			#pegar aqui os dados da reclamacao e salvar no banco
			assunto = request.form['assunto']
			mensagem = request.form['mensagem']
			nova_reclamacao = Mensagem()
			db.session.add(new_question)
			db.session.commit()
			flash('Reclamacao Enviada!')
		return render_template('contato.html')

if __name__ == '__main__':
        app.debug = True
        app.run(host='0.0.0.0')
