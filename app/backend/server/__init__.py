import sys
from flask import (
    Flask,
    abort,
    jsonify,
    request,
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin, current_user, login_user, logout_user, login_required
from flask_cors import CORS, cross_origin
from models import setup_db, usuario, producto, pedido, detallesPedido

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    CORS(app, origins =['http://127.0.0.1:5000', 'http://localhost:8080'], max_age=10)

    @app.after_request
    def after_resquest(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
    
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

    db = SQLAlchemy(app)

    if len(producto.query.all()) == 0:
        db.session.add_all([pAjo2,
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
                        SpP])
        db.session.commit()
    
    @app.route('/login', methods = ['POST'])
    def login():
        #body=request.get_json()
        username = request.get_json()['username']
        password = request.get_json()['password']
        
        user = usuario.query.filter(usuario.usuario == username).filter(usuario.contrasena == password).first()

        if user is None:
            abort(403)
        else:
            return jsonify({
                'success': True,
                'profile': {
                    'usuario': username
                }
            })
    
    @app.route('/users', methods=['GET'])
    def get_users():
        selection= usuario.query.order_by('id').all()
        usuarios= [user.format() for user in selection]

        if len(selection)==0:
            abort(404)

        return jsonify({
            'success':True,
            'usuarios': usuarios,
            'total_usuarios':len(selection)
        })

    @app.route('/users', methods = ['POST'])
    def insert_users():

        username = request.get_json()['username']
        password = request.get_json()['password']
        nombre = request.get_json()['name'] 
        apellido = request.get_json()['lastname']       
        email = request.get_json()['email']
        direccion = request.get_json()['adress']
        telefono = request.get_json()['phone']

        print(nombre)

        if nombre is '':
            abort(422)
        
        user = usuario(usuario=username,contrasena=password,nombre=nombre,apellido=apellido,email=email,direccion=direccion,telefono=telefono)
        new_user_id= user.insert()
        selection= usuario.query.order_by('id').all()
        current_users= [user.format() for user in selection]

        return jsonify({
            'success':True,
            'created':new_user_id,
            'peliculas': current_users,
            'total_peliculas': len(selection)
        })


    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success':False,
            'code':404,
            'message':'resource not found'
        }),404

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify({
            'success':False,
            'code':403,
            'message':'Forbidden'
        }),403
    
    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            'success':False,
            'code':500,
            'message':'Internal Server Error'
        }),500
    
    @app.errorhandler(422)
    def not_found_resource(error):
        return jsonify({
            'success':False,
            'code':422,
            'message':'resource not found'
        }),422

    return app
