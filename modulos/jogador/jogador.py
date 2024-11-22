from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Jogador

bp_jogador = Blueprint('jogador', __name__, template_folder='templates')

@bp_jogador.route('/')
def index():
    dados = Jogador.query.all()
    return render_template('jogador.html', dados=dados)

@bp_jogador.route('/add')
def add():
    return render_template('jogador_add.html')

@bp_jogador.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    posicao = request.form.get('posicao')
    if nome and posicao:
        objeto = Jogador(nome, posicao)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/jogador')
    else:
        flash('Preencha todos os campos!')
        return redirect('/jogador/add')

@bp_jogador.route("/remove/<int:id>")
def remove(id):
    dados = Jogador.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Jogador removido com sucesso!')
        return redirect("/jogador")
    else:
        flash("Caminho incorreto!")
        return redirect("/jogador")

@bp_jogador.route("/edita/<int:id>")
def edita(id):
    jogador = Jogador.query.get(id)
    return render_template("jogador_edita.html", dados=jogador)

@bp_jogador.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    posicao = request.form.get('posicao')
    if id and nome and posicao:
        time = Jogador.query.get(id)
        time.nome = nome
        time.posicao = posicao
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/jogador')
    else:
        flash('Dados incompletos.')
        return redirect("/jogador")