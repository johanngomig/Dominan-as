from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from models.models import Usuario
from config.config import db
from werkzeug.security import check_password_hash

auth_blueprint = Blueprint('auth', __name__)

@auth_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Aqui vai o seu cadastro
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        
        if Usuario.query.filter_by(email=email).first():
            flash('Usuário já registrado com esse email!', 'danger')
        
        novo_usuario = Usuario(
            nome=nome,
            email=email,
        )
        novo_usuario.set_senha(senha)
        
        db.session.add(novo_usuario)
        db.session.commit()
        
        flash('Registro realizado com sucesso!', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('register.html')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Aqui vai o seu login
        email = request.form['email']
        senha = request.form['senha']
        
        # user = Usuario.query.filter_by(email=email, senha=generate_password_hash(senha)).first()
        user = Usuario.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.senha, senha):
            session['user_id'] = user.id
            
            flash('Login efetuado com sucesso!', 'success')
            return redirect(url_for('dashboard.dashboard'))
        
        flash('Email ou senha inválidos', 'danger')
        
    return render_template('login.html')

@auth_blueprint.route('/logout')
def logout():
    #session.pop('user_id', None)
    session.clear()
    
    flash('Logout efetuado com sucesso!', 'success')
    return redirect(url_for('auth.login'))
        