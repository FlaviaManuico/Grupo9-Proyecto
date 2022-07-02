from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager,UserMixin, current_user, login_user, logout_user, login_required

database_name='pizza'
database_path='postgresql://{}@{}/{}'.format('postgres', 'localhost:5432', database_name)
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI']=database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app=app
    db.init_app(app) #para inicializar la aplicación :D XD
    db.create_all() #metodo para verificar si existe o no

class usuario(UserMixin,db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(), nullable=False)
    contrasena = db.Column(db.String(), nullable=False)
    nombre = db.Column(db.String(), nullable=False)
    apellido = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    direccion = db.Column(db.String(), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    pedidos = db.relationship('pedido', backref='user', lazy=True)

    def __init__(
            self,
            usuario,
            contrasena,
            nombre,
            apellido,
            email,
            direccion,
            telefono):
        self.usuario = usuario
        self.contrasena = self.create_password(contrasena)
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.direccion = direccion
        self.telefono = telefono

    def create_password(self, password):
        return generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.contrasena, password)

    def __repr__(self):
        return f'Usuario: id={self.id}, usuario={self.usuario}, contrasena={self.contrasena}, nombre={self.nombre}, apellido={self.apellido}, email={self.email}, direccion={self.direccion}, telefono={self.telefono}'
