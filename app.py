from flask import Flask, render_template
app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdt435t4654756h3q3464756y'
conexao = 'mysql+pymysql://alunos:cefetmg@127.0.0.1/jogadores_times'
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
db.init_app(app)
migrate = Migrate(app, db)
from models import Jogador, Time
from modulos.jogador.jogador import bp_jogador
from modulos.time.time import bp_time
app.register_blueprint(bp_jogador, url_prefix='/jogador')
app.register_blueprint(bp_time, url_prefix='/time')
@app.route('/')
def index():
    return render_template('ola.html')