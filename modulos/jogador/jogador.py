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

EDITAR
@bp_time.route("/remove/<int:id>")
def remove(id):
    dados = Time.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Time removido com sucesso!')
        return redirect("/time")
    else:
        flash("Caminho incorreto!")
        return redirect("/time")

@bp_time.route("/edita/<int:id>")
def edita(id):
    time = Time.query.get(id)
    return render_template("time_edita.html", dados=time)

@bp_time.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    cidade = request.form.get('cidade')
    if id and nome and cidade:
        jogador = Time.query.get(id)
        jogador.nome = nome
        jogador.cidade = cidade
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/time')
    else:
        flash('Dados incompletos.')
        return redirect("/time")