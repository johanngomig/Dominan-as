from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from models.models import ContaPagar, ContaReceber, CompraCartaoCredito, Usuario
from config.config import db
from datetime import datetime
from dateutil.relativedelta import relativedelta

relatorios_blueprint = Blueprint('report', __name__)

@relatorios_blueprint.route('/relatorios', methods=['GET', 'POST'])
def relatorios():
    usuario_id = session.get('user_id')
    usuario = Usuario.query.filter_by(id=usuario_id).first()

    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))

    tipo_relatorio = request.args.get('tipo_relatorio', 'despesas_categoria')
    data_inicial = request.args.get('data_inicial', datetime.today().strftime('%Y-%m-%d'))
    data_final = request.args.get('data_final', (datetime.today() + relativedelta(months=+1)).strftime('%Y-%m-%d'))

    if tipo_relatorio == 'despesas_categoria':
        despesas_cartao = db.session.query(CompraCartaoCredito.categoria, db.func.sum(CompraCartaoCredito.valor)).filter(
            CompraCartaoCredito.usuario_id == usuario_id,
            CompraCartaoCredito.data_compra.between(data_inicial, data_final)
        ).group_by(CompraCartaoCredito.categoria).all()

        despesas_pagar = db.session.query(ContaPagar.categoria, db.func.sum(ContaPagar.valor)).filter(
            ContaPagar.usuario_id == usuario_id,
            ContaPagar.data_vencimento.between(data_inicial, data_final)
        ).group_by(ContaPagar.categoria).all()

        despesas_receber = db.session.query(ContaReceber.categoria, db.func.sum(ContaReceber.valor)).filter(
            ContaReceber.usuario_id == usuario_id,
            ContaReceber.data_recebimento.between(data_inicial, data_final)
        ).group_by(ContaReceber.categoria).all()

        categorias = {}
        
        for categoria, valor in despesas_cartao:
            if categoria in categorias:
                categorias[categoria] += valor
            else:
                categorias[categoria] = valor

        for categoria, valor in despesas_pagar:
            if categoria in categorias:
                categorias[categoria] += valor
            else:
                categorias[categoria] = valor

        for categoria, valor in despesas_receber:
            if categoria in categorias:
                categorias[categoria] += valor
            else:
                categorias[categoria] = valor

        labels = list(categorias.keys())
        valores = list(categorias.values())


    elif tipo_relatorio == 'saldo_pagar_receber':
        total_pagar = db.session.query(db.func.sum(ContaPagar.valor)).filter(
            ContaPagar.usuario_id == usuario_id,
            ContaPagar.data_vencimento.between(data_inicial, data_final)
        ).scalar() or 0

        total_receber = db.session.query(db.func.sum(ContaReceber.valor)).filter(
            ContaReceber.usuario_id == usuario_id,
            ContaReceber.data_recebimento.between(data_inicial, data_final)
        ).scalar() or 0

        total_compras_cartao = db.session.query(db.func.sum(CompraCartaoCredito.valor)).filter(
            CompraCartaoCredito.usuario_id == usuario_id,
            CompraCartaoCredito.data_compra.between(data_inicial, data_final)
        ).scalar() or 0

        labels = ['Contas a Pagar', 'Contas a Receber', 'Compras com Cartão']
        valores = [total_pagar, total_receber, total_compras_cartao]


    return render_template('relatorios.html', 
                           labels=labels, 
                           valores=valores,
                           tipo_relatorio=tipo_relatorio,
                           data_inicial=data_inicial,
                           data_final=data_final,
                           usuario=usuario)
