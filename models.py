from database import db

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(15))

    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __repr__(self):
        return '<Cliente {}>'.format(self.nome)



class Reclamacao(db.Model):
    __tablename__ = 'reclamacao'
    id = db.Column(db.Integer, primary_key = True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    descricao = db.Column(db.String(225))
    data = db.Column(db.Date)   

    cliente = db.relationship('Cliente', foreign_keys = cliente_id)

    def __init__(self, descricao, data, cliente_id):
        self.descricao = descricao
        self.data = data
        self.cliente_id = cliente_id

    def __repr__(self):
        return '<Reclamações {}>'.format(self.descricao)
    
    