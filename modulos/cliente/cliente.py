from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Cliente

bp_cliente = Blueprint('cliente', __name__, template_folder='templates')

@bp_cliente.route('/')
def index():
    dados = Cliente.query.all()
    return render_template('cliente.html', dados=dados)

@bp_cliente.route('/add')
def add():
    return render_template('cliente_add.html')

@bp_cliente.route('/save', methods=['POST'])
def save():
    nome = request.form.get('nome')
    telefone = request.form.get('telefone')
    if nome and telefone:
        objeto = Cliente(nome, telefone)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/cliente')
    else:
        flash('Preencha todos os campos!')
        return redirect('/cliente/add')
