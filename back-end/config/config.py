import os
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

DATABASE_URL = os.getenv("DATABASE_URL",'postgresql://postgres:postgres@localhost:5433/controle_financeiro')

class Config():
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', '9eb71ab7420eb452a22787ca4fab501b')
    
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)

db = SQLAlchemy()