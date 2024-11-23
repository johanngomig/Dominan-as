from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from models.models import ContaPagar, ContaReceber, Usuario
from config.config import db

account_blueprint = Blueprint('account', __name__)

@account_blueprint.route('/contas_a_pagar')
def contas_a_pagar():
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    contas = ContaPagar.query.filter_by(usuario_id=usuario_id).all()
    
    return render_template('contas_a_pagar.html', contas=contas, usuario=usuario)

@account_blueprint.route('/contas_a_pagar/nova', methods=['GET', 'POST'])
def nova_conta_a_pagar():
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    
    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        data_vencimento = request.form['data_vencimento']
        categoria = request.form['categoria']
        usuario_id = session.get('user_id')
        
        status = "status" in request.form
        
        nova_conta = ContaPagar(
            descricao=descricao, 
            valor=valor, 
            data_vencimento=data_vencimento, 
            categoria=categoria, 
            status=status,
            usuario_id=usuario_id
        )

        db.session.add(nova_conta)
        db.session.commit()
        
        flash('Conta a pagar registrada com sucesso', 'success')
        return redirect(url_for('account.contas_a_pagar'))
    
    return render_template('nova_conta_a_pagar.html', usuario=usuario)

@account_blueprint.route('/contas_a_pagar/editar/<conta_id>', methods=['GET', 'POST'])
def editar_conta_a_pagar(conta_id):
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    conta = ContaPagar.query.filter_by(id=conta_id, usuario_id=usuario_id).first()
    
    if request.method == 'POST':
        conta.descricao = request.form['descricao']
        conta.valor = request.form['valor']
        conta.data_vencimento = request.form['data_vencimento']
        conta.categoria = request.form['categoria']
        conta.status = "status" in request.form
        
        db.session.commit()
        
        flash('Conta a pagar editada com sucesso', 'success')
        return redirect(url_for('account.contas_a_pagar'))
    
    return render_template('editar_conta_a_pagar.html', conta=conta, usuario=usuario)

@account_blueprint.route('/contas_a_pagar/excluir/<conta_id>', methods=['POST'])
def excluir_conta_a_pagar(conta_id):
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    conta = ContaPagar.query.filter_by(id=conta_id, usuario_id=usuario_id).first()
    
    if not conta:
        flash('Conta não encontrada', 'danger')
        return redirect(url_for('account.contas_a_pagar'))
    
    db.session.delete(conta)
    db.session.commit()
    
    flash('Conta excluída com sucesso', 'success')
    return redirect(url_for('account.contas_a_pagar'))

@account_blueprint.route('/contas_a_receber')
def contas_a_receber():
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    contas = ContaReceber.query.filter_by(usuario_id=usuario_id).all()
    
    return render_template('contas_a_receber.html', contas_receber=contas, usuario=usuario)

@account_blueprint.route('/contas_a_receber/nova', methods=['GET', 'POST'])
def nova_conta_a_receber():
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()

    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = request.form['valor']
        data_recebimento = request.form['data_recebimento']
        categoria = request.form['categoria']
        usuario_id = session.get('user_id')
        
        status = "status" in request.form
        
        nova_conta = ContaReceber(
            descricao=descricao, 
            valor=valor, 
            data_recebimento=data_recebimento, 
            categoria=categoria, 
            status=status,
            usuario_id=usuario_id
        )

        db.session.add(nova_conta)
        db.session.commit()
        
        flash('Conta a receber registrada com sucesso', 'success')
        return redirect(url_for('account.contas_a_receber'))
    
    return render_template('nova_conta_a_receber.html', usuario=usuario)

@account_blueprint.route('/contas_a_receber/editar/<conta_id>', methods=['GET', 'POST'])
def editar_conta_a_receber(conta_id):
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    conta = ContaReceber.query.filter_by(id=conta_id, usuario_id=usuario_id).first()
    
    if not conta:
        flash('Conta não encontrada', 'danger')
        return redirect(url_for('account.contas_a_receber'))
    
    if request.method == 'POST':
        conta.descricao = request.form['descricao']
        conta.valor = request.form['valor']
        conta.data_recebimento = request.form['data_recebimento']
        conta.categoria = request.form['categoria']
        conta.status = "status" in request.form
        
        db.session.commit()
        
        flash('Conta a receber editada com sucesso', 'success')
        return redirect(url_for('account.contas_a_receber'))
    
    return render_template('editar_conta_a_receber.html', conta=conta, usuario=usuario)

@account_blueprint.route('/contas_a_receber/excluir/<conta_id>', methods=['POST'])
def excluir_conta_a_receber(conta_id):
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    conta = ContaReceber.query.filter_by(id=conta_id, usuario_id=usuario_id).first()
    
    if not conta:
        flash('Conta não encontrada', 'danger')
        return redirect(url_for('account.contas_a_receber'))
    
    db.session.delete(conta)
    db.session.commit()
    
    flash('Conta excluída com sucesso', 'success')
    return redirect(url_for('account.contas_a_receber'))