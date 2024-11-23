from flask import Blueprint, render_template, session, redirect, url_for, flash
from models.models import ContaPagar, ContaReceber, CompraCartaoCredito, Usuario
from config.config import db
from datetime import datetime

dashboard_blueprint = Blueprint('dashboard', __name__)

@dashboard_blueprint.route('/dashboard')
def dashboard():
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()

    total_contas_a_pagar = db.session.query(db.func.sum(ContaPagar.valor)).filter_by(usuario_id=usuario_id, status=False).scalar() or 0
    total_contas_a_pagar += db.session.query((db.func.sum(CompraCartaoCredito.valor)).filter(
        CompraCartaoCredito.usuario_id == usuario_id,
        CompraCartaoCredito.data_compra > datetime.today().strftime('%Y-%m-%d'))
    ).scalar() or 0
    
    total_contas_pagas = db.session.query(db.func.sum(ContaPagar.valor)).filter_by(usuario_id=usuario_id, status=True).scalar() or 0
    total_contas_pagas += db.session.query((db.func.sum(CompraCartaoCredito.valor)).filter(
        CompraCartaoCredito.usuario_id == usuario_id,
        CompraCartaoCredito.data_compra < datetime.today().strftime('%Y-%m-%d'))
    ).scalar() or 0
    
    total_contas_a_receber = db.session.query(db.func.sum(ContaReceber.valor)).filter_by(usuario_id=usuario_id, status=False).scalar() or 0
    total_contas_recebidas = db.session.query(db.func.sum(ContaReceber.valor)).filter_by(usuario_id=usuario_id, status=True).scalar() or 0
    
    
    saldo_pago = total_contas_recebidas - total_contas_pagas
    saldo_pagar = total_contas_a_receber - total_contas_a_pagar


    return render_template('dashboard.html', 
                           total_contas_a_pagar=total_contas_a_pagar, 
                           total_contas_pagas=total_contas_pagas,
                           total_contas_a_receber=total_contas_a_receber,
                           total_contas_recebidas=total_contas_recebidas,
                           saldo_pago=saldo_pago,
                           saldo_pagar=saldo_pagar,
                           usuario=usuario)
