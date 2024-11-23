from config.config import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(255), nullable=False)
    data_criacao = db.Column(db.TIMESTAMP, server_default=db.func.now())
    
    def set_senha(self, senha):
        self.senha = generate_password_hash(senha)
        
    def check_senha(self, senha):
        return check_password_hash(self.senha, senha)

class ContaPagar(db.Model):
    __tablename__ = 'conta_a_pagar'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.Float(10, 2), nullable=False)
    data_vencimento = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, default=False)
    categoria = db.Column(db.String(50))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    

class ContaReceber(db.Model):
    __tablename__ = 'conta_a_receber'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.Float(10, 2), nullable=False)
    data_recebimento = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, default=False)
    categoria = db.Column(db.String(50))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

class CartaoCredito(db.Model):
    __tablename__ = 'cartao_credito'
    id = db.Column(db.Integer, primary_key=True)
    nome_cartao = db.Column(db.String(50), nullable=False)
    data_vencimento = db.Column(db.Date, nullable=False)
    limite_cartao = db.Column(db.Float(10, 2), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    # Relacionamento com as compras
    compras = db.relationship('CompraCartaoCredito', backref='cartao_credito', cascade="all, delete-orphan")


class CompraCartaoCredito(db.Model):
    __tablename__ = 'compra_cartao_credito'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(255), nullable=False)
    valor = db.Column(db.Float(10, 2), nullable=False)
    data_compra = db.Column(db.Date, nullable=False)
    categoria = db.Column(db.String(50))
    num_parcelas = db.Column(db.Integer, default=1)
    cartao_utilizado = db.Column(db.Integer, db.ForeignKey('cartao_credito.id', ondelete='CASCADE'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)

    # Relação com as parcelas
    parcelas = db.relationship('ParcelasCartao', backref='compra', cascade="all, delete-orphan")


class ParcelasCartao(db.Model):
    __tablename__ = 'parcelas_cartao'
    id = db.Column(db.Integer, primary_key=True)
    compra_id = db.Column(db.Integer, db.ForeignKey('compra_cartao_credito.id', ondelete='CASCADE'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'))
    numero_parcela = db.Column(db.Integer, nullable=False)
    valor_parcela = db.Column(db.Float(10, 2), nullable=False)
    data_parcela = db.Column(db.Date, nullable=False)

    usuario = db.relationship('Usuario', backref='parcelas_cartao')

class RelatorioFinanceiro(db.Model):
    __tablename__ = 'relatorio_financeiro'
    id = db.Column(db.Integer, primary_key=True)
    tipo_relatorio = db.Column(db.String(50), nullable=False)
    data_geracao = db.Column(db.TIMESTAMP, server_default=db.func.now())
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    
    usuario = db.relationship('Usuario', backref='relatorios')