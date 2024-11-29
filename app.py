from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdt435t4654756h3q3464756y'
conexao = 'mysql+pymysql://alunos:cefetmg@127.0.0.1/cliente_reclamacoes'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Cliente, Reclamacao
from modulos.cliente.cliente import bp_cliente
from modulos.reclamacao.reclamacao import bp_reclamacao
app.register_blueprint(bp_cliente, url_prefix='/cliente')
app.register_blueprint(bp_reclamacao, url_prefix='/reclamacao')
@app.route('/')
def index():
    return render_template('ola.html')