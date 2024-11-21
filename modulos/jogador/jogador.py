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
