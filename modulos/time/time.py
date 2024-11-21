from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Time, Jogador

bp_time = Blueprint('time', __name__, template_folder='templates')

@bp_time.route('/')
def index():
    dados = Time.query.all()
    return render_template('time.html', dados=dados)

@bp_time.route('/add')
def add():
    j = Jogador.query.all()
    return render_template('time_add.html', jogador = j)

@bp_time.route('/save', methods=['POST'])
def save():
    jogador_id = request.form.get('jogador_id')
    nome = request.form.get('nome')
    cidade = request.form.get('cidade')
    if jogador_id and nome and cidade:
        objeto = Time(jogador_id, nome, cidade)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/time')
    else:
        flash('Preencha todos os campos!')
        return redirect('/time/add')

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
    jogador = Jogador.query.all()
    return render_template("time_edita.html", dados=time, jogador=jogador)

@bp_time.route("/editasave", methods=['POST'])
def editasave():
    id = request.form.get('id')
    nome = request.form.get('nome')
    cidade = request.form.get('cidade')
    jogador_id = request.form.get('jogador_id')
    if id and nome and cidade and jogador_id:
        time = Time.query.get(id)
        time.nome = nome
        time.cidade = cidade
        time.jogador_id = jogador_id
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect('/time')
    else:
        flash('Dados incompletos.')
        return redirect("/time")