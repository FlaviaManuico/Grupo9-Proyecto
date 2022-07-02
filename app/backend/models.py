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


class producto(db.Model):
     __tablename__ = 'productos'
     id = db.Column(db.Integer, primary_key=True)
     comida = db.Column(db.String(), nullable=False)
     precio = db.Column(db.Float(), nullable=False)
     detalles = db.relationship('detallesPedido', backref='detalles0', lazy=True)


    
     def __repr__(self):
        return f'Producto: id={self.id} comida={self.comida}, precio={self.precio}'

class pedido(db.Model):
     __tablename__ = 'pedidos'
     id = db.Column(db.Integer(), primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
     fechaPedido = db.Column(db.DateTime, default=datetime.now())
     detalle = db.relationship('detallesPedido', backref='detalles', lazy=True)

     def __repr__(self):
         return f'Pedido: id={self.id} fechaPedido={self.fechaPedido}'

class detallesPedido(db.Model):
    __tablename__ = 'detalles_pedidos'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad= db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Carrito: id={self.id}, cantidad={self.cantidad}'
        

# PRODUCTOS
# Entradas
pAjo2 = producto(comida='Pan al Ajo (x2)', precio=4.00)
pAjo4 = producto(comida='Pan al Ajo (x4)', precio=8.00)
pQueso2 = producto(comida='Palitos de Queso (x2)', precio=5.50)
pQueso4 = producto(comida='Palitos de Queso (x4)', precio=11.00)

# Pizzas
PHf = producto(comida='Pizza Hawaiana Familiar', precio=32.90)
PHg = producto(comida='Pizza Hawaiana Grande', precio=22.90)
PHm = producto(comida='Pizza Hawaiana Mediana', precio=16.90)
PHp = producto(comida='Pizza Hawaiana Personal', precio=10.00)
PAf = producto(comida='Pizza Americana Familiar', precio=29.90)
PAg = producto(comida='Pizza Americana Grande', precio=19.90)
PAm = producto(comida='Pizza Americana Mediana', precio=13.90)
PAp = producto(comida='Pizza Americana Personal', precio=7.00)
PPf = producto(comida='Pizza de Pepperoni Familiar', precio=30.90)
PPg = producto(comida='Pizza de Pepperoni Grande', precio=20.90)
PPm = producto(comida='Pizza de Pepperoni Mediana', precio=14.90)
PPp = producto(comida='Pizza de Pepperoni Personal', precio=8.00)
PMf = producto(comida='Pizza Mozarella Familiar', precio=31.90)
PMg = producto(comida='Pizza Mozarella Grande', precio=21.90)
PMm = producto(comida='Pizza Mozarella Mediana', precio=15.90)
PMp = producto(comida='Pizza Mozarella Personal', precio=9.00)

# Lasagnas
lVegetariana = producto(comida='Lasagna Vegetariana', precio=22.90)
lCarne = producto(comida='Lasagna de Carne', precio=20.90)
lHawaiana = producto(comida='Lasagna Hawaiana', precio=22.90)
lQueso = producto(comida='Lasagna de 4 Quesos', precio=24.90)
lChamp = producto(comida='Lasagna de Champiñones', precio=25.90)

# Bebidas
CPersonal = producto(comida='Coca Cola Personal', precio=2.50)
InP = producto(comida='Inca Kola Personal', precio=2.50)
FaP = producto(comida='Fanta Personal', precio=3.20)
SpP = producto(comida='Sprite Personal', precio=3.20)

array_productos=[
    pAjo2,
    pAjo4,
    pQueso2,
    pQueso4,
    PHf,
    PHg,
    PHm,
    PHp,
    PAf,
    PAg,
    PAm,
    PAp,
    PPf,
    PPg,
    PPm,
    PPp,
    PMf,
    PMg,
    PMm,
    PMp,
    lVegetariana,
    lCarne,
    lHawaiana,
    lQueso,
    lChamp,
    CPersonal,
    InP,
    FaP,
    SpP
]