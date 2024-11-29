from flask import Blueprint, render_template, request, redirect, flash
from database import db 
from models import Reclamacao, Cliente

bp_reclamacao = Blueprint('reclamacao', __name__, template_folder='templates')

@bp_reclamacao.route('/')
def index():
    dados = Reclamacao.query.all()
    return render_template('reclamacao.html', dados=dados)

@bp_reclamacao.route('/add')
def add():
    c = Cliente.query.all()
    return render_template('reclamacao_add.html', cliente = c)

@bp_reclamacao.route('/save', methods=['POST'])
def save():
    descricao = request.form.get('descricao')
    data = request.form.get('data')
    cliente_id = request.form.get('cliente_id')
    if descricao and data and cliente_id:
        objeto = Cliente(descricao, data, cliente_id)
        db.session.add(objeto)
        db.session.commit()
        flash('Salvo!')
        return redirect('/reclamacao')
    else:
        flash('Preencha todos os campos!')
        return redirect('/reclamacao/add')

@bp_reclamacao.route("/remove/<int:id>")
def remove(id):
    dados = Cliente.query.get(id)
    if id > 0:
        db.session.delete(dados)
        db.session.commit()
        flash('Reclamação removida com sucesso!')
        return redirect("/reclamacao")
    else:
        flash("Caminho incorreto!")
        return redirect("/reclamacao")
