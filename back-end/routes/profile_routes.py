from flask import Blueprint, render_template, session, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models.models import Usuario
from config.config import db

profile_blueprint = Blueprint('profile', __name__)

@profile_blueprint.route('/perfil_usuario', methods=['GET', 'POST'])
def perfil_usuario():
    usuario_id = session.get('user_id')

    # Verifica se o usuário está logado
    if not usuario_id:
        flash('Usuário não logado', 'danger')
        return redirect(url_for('auth.login'))

    usuario = Usuario.query.filter_by(id=usuario_id).first()

    if request.method == 'POST':
        usuario.nome = request.form['nome']
        usuario.email = request.form['email']
        
        senha_atual = request.form.get('senha_atual')
        nova_senha = request.form.get('nova_senha')

        # Atualizando a senha, se uma nova senha for fornecida
        if senha_atual and nova_senha:
            if check_password_hash(usuario.senha, senha_atual):
                usuario.senha = generate_password_hash(nova_senha)
                flash('Senha atualizada com sucesso!', 'success')
            else:
                flash('Senha atual incorreta.', 'danger')
                return redirect(url_for('profile.perfil_usuario'))

        db.session.commit()

        flash('Perfil atualizado com sucesso!', 'success')
        return redirect(url_for('profile.perfil_usuario'))

    return render_template('perfil_usuario.html', usuario=usuario)
