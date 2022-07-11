from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

database_name='pizza'
database_path='postgresql://{}:@{}/{}'.format('postgres', 'localhost:5432', database_name)
db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config['SQLALCHEMY_DATABASE_URI']=database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app=app
    db.init_app(app) #para inicializar la aplicación
    db.create_all() #metodo para verificar si existe o no

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(), nullable=False)
    contrasena = db.Column(db.String(), nullable=False)
    nombre = db.Column(db.String(), nullable=False)
    apellido = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    direccion = db.Column(db.String(), nullable=False)
    telefono = db.Column(db.Integer, nullable=False)
    pedidos = db.relationship('Pedido', backref='user', lazy=True)

    def format(self):
        return{
            'id': self.id,
            'ususario': self.usuario,
            'contrasena': self.contrasena,
            'nombre': self.nombre,
            'apellido':self.apellido,
            'email':self.email,
            'direccion':self.direccion,
            'telefono':self.telefono
        }

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

    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()

class Producto(db.Model):
     __tablename__ = 'productos'
     id = db.Column(db.Integer, primary_key=True)
     comida = db.Column(db.String(), nullable=False)
     precio = db.Column(db.Float(), nullable=False)
     detalles = db.relationship('DetallesPedido', backref='detalles0', lazy=True)

     def format(self):
        return{
            'id': self.id,
            'comida': self.comida,
            'precio': self.precio,
        }

     def __repr__(self):
        return f'Producto: id={self.id} comida={self.comida}, precio={self.precio}'

class Pedido(db.Model):
     __tablename__ = 'pedidos'
     id = db.Column(db.Integer(), primary_key=True)
     user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
     fechaPedido = db.Column(db.DateTime, default=datetime.now())
     detalle = db.relationship('DetallesPedido', backref='detalles', lazy=True)
    
     def format(self):
        return{
            'id': self.id,
            'user_id': self.user_id,
            'fechaPedido': self.fechaPedido,
        }

     def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()
     
     def __repr__(self):
         return f'Pedido: id={self.id} fechaPedido={self.fechaPedido}'

class DetallesPedido(db.Model):
    __tablename__ = 'detalles_pedidos'
    id = db.Column(db.Integer, primary_key=True)
    pedido_id = db.Column(db.Integer, db.ForeignKey('pedidos.id'), nullable=False)
    producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'), nullable=False)
    cantidad= db.Column(db.Integer, default=1)

    def format(self):
        return{
            'id': self.id,
            'pedido_id': self.pedido_id,
            'producto_id': self.producto_id,
            'cantidad': self.cantidad,
        }
    
    def insert(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self.id
        except:
            db.session.rollback()
        finally:
            db.session.close()

    def __repr__(self):
        return f'Carrito: id={self.id}, cantidad={self.cantidad}'
        
