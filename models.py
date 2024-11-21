from database import db

class Jogador(db.Model):
    __tablename__ = 'jogador'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    posicao = db.Column(db.String(50))

    def __init__(self, nome, posicao):
        self.nome = nome
        self.posicao = posicao

    def __repr__(self):
        return '<Jogador {}>'.format(self.nome)



class Time(db.Model):
    __tablename__ = 'time'
    id = db.Column(db.Integer, primary_key = True)
    jogador_id = db.Column(db.Integer, db.ForeignKey('jogador.id'))
    nome = db.Column(db.String(100))
    cidade = db.Column(db.String(50))   

    jogador = db.relationship('Jogador', foreign_keys = jogador_id)

    def __init__(self, jogador_id, nome, cidade):
        self.jogador_id = jogador_id
        self.nome = nome
        self.cidade = cidade

    def __repr__(self):
        return '<Time {}>'.format(self.nome)
    
    