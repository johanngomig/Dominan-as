from flask import Blueprint, render_template, session, redirect, request, url_for, flash
from models.models import CompraCartaoCredito, ParcelasCartao, Usuario, CartaoCredito
from config.config import db
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from decimal import Decimal

card_blueprint = Blueprint('card', __name__)

@card_blueprint.route('/compras_cartao')
def compras_cartao():
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    compras = CompraCartaoCredito.query.filter_by(usuario_id=usuario_id).all()
    
    compras_com_nome_cartao = []
    
    for compra in compras:
        cartao = CartaoCredito.query.filter_by(id=compra.cartao_utilizado).first()
        compras_com_nome_cartao.append({
            'id': compra.id,
            'descricao': compra.descricao,
            'valor': compra.valor,
            'data_compra': compra.data_compra,
            'categoria': compra.categoria,
            'num_parcelas': compra.num_parcelas,
            'cartao_utilizado':compra.cartao_utilizado,
            'nome_cartao':cartao.nome_cartao,
            'usuario_id':compra.usuario_id
        })
        
    return render_template('compras_cartao.html', compras=compras_com_nome_cartao, usuario=usuario)

@card_blueprint.route('/compras_cartao/nova', methods=['GET', 'POST'])
def nova_compra_cartao():
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    cartoes = CartaoCredito.query.filter_by(usuario_id=usuario_id).all()
    
    if not cartoes:
        flash('Nenhum cartão encontrado, por favor cadastre um cartão', 'danger')
        return redirect(url_for('card.compras_cartao'))
    
    cartoes_com_limite_restante = []
    
    for cartao in cartoes:
 
        total_gasto_atual = db.session.query(db.func.sum(CompraCartaoCredito.valor)).filter_by(cartao_utilizado=cartao.id, usuario_id=usuario_id).scalar() or Decimal(0)
        limite_restante = cartao.limite_cartao - total_gasto_atual
        
        cartoes_com_limite_restante.append({
            'id':cartao.id,
            'nome_cartao':cartao.nome_cartao,
            'limite_cartao':cartao.limite_cartao,
            'limite_restante':limite_restante,
            'data_vencimento':cartao.data_vencimento
        })

    if request.method == 'POST':
        descricao = request.form['descricao']
        valor = Decimal(request.form['valor'])
        data_compra = request.form['data_compra']
        categoria = request.form['categoria']
        num_parcelas = int(request.form['parcelas'])
        cartao_utilizado = int(request.form['cartao_utilizado'])
        
        cartao = CartaoCredito.query.filter_by(id=cartao_utilizado, usuario_id=usuario_id).first()
        total_gasto_atual = db.session.query(db.func.sum(CompraCartaoCredito.valor)).filter_by(cartao_utilizado=cartao_utilizado, usuario_id=usuario_id).scalar() or 0
        
        limite_restante = cartao.limite_cartao - total_gasto_atual
        
        compra = ({
            'descricao':descricao,
            'valor':valor,
            'data_compra':data_compra,
            'categoria':categoria,
            'num_parcelas':num_parcelas,
            'cartao_utilizado':cartao_utilizado
        })
        
        if valor > limite_restante:
            flash('O valor da compra ultrapassa o limite disponível neste cartão', 'danger')
            # return redirect(url_for('card.compras_cartao'))
            return render_template('nova_compra_cartao.html', usuario=usuario, compra=compra, cartoes=cartoes_com_limite_restante)
        
        nova_compra = CompraCartaoCredito(
            descricao=descricao, 
            valor=valor, 
            data_compra=data_compra, 
            categoria=categoria, 
            num_parcelas=num_parcelas, 
            cartao_utilizado=cartao_utilizado, 
            usuario_id=usuario_id
        )

        db.session.add(nova_compra)
        db.session.commit()
        
        valor_parcela = valor / num_parcelas
        for i in range(1, num_parcelas + 1):
            data_parcela = datetime.strptime(data_compra, '%Y-%m-%d') + relativedelta(months=i-1)
            parcela = ParcelasCartao(
                compra_id=nova_compra.id,
                usuario_id=usuario_id,
                numero_parcela=i,
                valor_parcela=valor_parcela,
                data_parcela=data_parcela
            )
            db.session.add(parcela)
                
        db.session.commit()
        
        flash('Compra adicionada com sucesso', 'success')
        return redirect(url_for('card.compras_cartao'))
    
    return render_template('nova_compra_cartao.html', usuario=usuario, cartoes=cartoes_com_limite_restante)

@card_blueprint.route('/compras_cartao/excluir/<int:compra_id>', methods=['POST'])
def excluir_compra_cartao(compra_id):
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    compra = CompraCartaoCredito.query.filter_by(id=compra_id, usuario_id=usuario_id).first()
    
    if not compra:
        flash('Compra não encontrada', 'danger')
        return redirect(url_for('card.compras_cartao'))
    
    db.session.delete(compra)
    db.session.commit()
    
    flash('Compra excluída com sucesso', 'success')
    return redirect(url_for('card.compras_cartao'))

@card_blueprint.route('/compras_cartao/<int:compra_id>/parcelas')
def visualizar_parcelas(compra_id):
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    
    compra = CompraCartaoCredito.query.filter_by(id=compra_id, usuario_id=usuario_id).first()
    if not compra:
        flash('Compra não encontrada', 'danger')
        return redirect(url_for('card.compras_cartao'))
    
    parcelas = ParcelasCartao.query.filter_by(compra_id=compra_id, usuario_id=usuario_id).all()

    data_hoje = datetime.today().date()
    
    for parcela in parcelas:
        if parcela.data_parcela < data_hoje:
          parcela.status = 'Vencida'
        elif parcela.data_parcela == data_hoje:
          parcela.status = 'Vencimento hoje'
        elif parcela.data_parcela <= data_hoje + timedelta(days=7):  # Inclui até o sétimo dia
         parcela.status = 'Vencimento em breve'
        else:
           parcela.status = 'Em dia'
    
    return render_template('parcelas_cartao.html', compra=compra, parcelas=parcelas, usuario=usuario)


@card_blueprint.route('/cartoes_credito')
def cartoes_credito():
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    cartoes = CartaoCredito.query.filter_by(usuario_id=usuario_id).all()
    
    cartoes_com_limite_restante = []
    
    for cartao in cartoes:
        limite_cartao = Decimal(cartao.limite_cartao)
        total_gasto = db.session.query(db.func.sum(CompraCartaoCredito.valor)).filter_by(cartao_utilizado=cartao.id, usuario_id=usuario_id).scalar() or Decimal(0)
        limite_restante = limite_cartao - total_gasto
        
        cartoes_com_limite_restante.append({
            'id':cartao.id,
            'nome_cartao':cartao.nome_cartao,
            'limite_cartao':cartao.limite_cartao,
            'limite_restante':limite_restante,
            'data_vencimento':cartao.data_vencimento
        })
    
    return render_template('cartoes_credito.html',usuario=usuario, cartoes=cartoes_com_limite_restante)

@card_blueprint.route('/cartao_credito/novo', methods=['GET', 'POST'])
def novo_cartao_credito():
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    cartoes = CartaoCredito.query.filter_by(usuario_id=usuario_id).all()
    
    if request.method == 'POST':
        nome_cartao = request.form['nome_cartao']
        limite_cartao = float(request.form['limite_cartao'])
        data_vencimento = request.form['data_vencimento']
        
        novo_cartao = CartaoCredito(
            nome_cartao=nome_cartao, 
            limite_cartao=limite_cartao, 
            usuario_id=usuario_id,
            data_vencimento=data_vencimento
        )
        
        db.session.add(novo_cartao)
        db.session.commit()
        
        flash('Cartão cadastrado com sucesso', 'success')
        return redirect(url_for('card.cartoes_credito'))
    
    return render_template('novo_cartao_credito.html', cartoes=cartoes, usuario=usuario)


@card_blueprint.route('/cartao_credito/editar/<int:cartao_id>', methods=['GET', 'POST'])
def editar_cartao_credito(cartao_id):
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    usuario = Usuario.query.filter_by(id=usuario_id).first()
    cartao = CartaoCredito.query.filter_by(id=cartao_id, usuario_id=usuario_id).first()
    
    if not cartao:
        flash('Cartão não encontrado', 'danger')
        return redirect(url_for('card.cartoes_credito'))

    if request.method == 'POST':
        
        if float(request.form['limite_cartao']) < cartao.limite_cartao:
            flash('Não é possível reduzir o limite do cartão', 'danger')
            return redirect(url_for('card.cartoes_credito'))
    
        cartao.nome_cartao = request.form['nome_cartao']
        cartao.limite_cartao = float(request.form['limite_cartao'])
        cartao.data_vencimento = request.form['data_vencimento']

        db.session.commit()
        
        flash('Cartão atualizado com sucesso', 'success')
        return redirect(url_for('card.cartoes_credito'))
    
    return render_template('editar_cartao_credito.html', cartao=cartao, usuario=usuario)

@card_blueprint.route('/cartao_credito/excluir/<int:cartao_id>', methods=['GET', 'POST'])
def excluir_cartao_credito(cartao_id):
    usuario_id = session.get('user_id')
    
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))
    
    cartao = CartaoCredito.query.filter_by(id=cartao_id, usuario_id=usuario_id).first()
    
    if not cartao:
        flash('Cartão não encontrado', 'danger')
        return redirect(url_for('card.cartoes_credito'))
    
    compras = db.session.query(CompraCartaoCredito).filter_by(cartao_utilizado=cartao_id, usuario_id=usuario_id).all()
    
    if compras:
        flash('Cartão não pode ser excluído, existem compras relacionadas', 'danger')
        return redirect(url_for('card.cartoes_credito'))
    
    db.session.delete(cartao)
    db.session.commit()
    
    flash('Cartão excluído com sucesso', 'success')
    return redirect(url_for('card.cartoes_credito'))
