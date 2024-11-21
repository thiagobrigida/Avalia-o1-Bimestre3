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