import sys
from flask import (
    Flask,
    abort,
    jsonify,
    request,
)
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Usuario, Producto, Pedido, DetallesPedido

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
    pAjo2 = Producto(comida='Pan al Ajo (x2)', precio=4.00)
    pAjo4 = Producto(comida='Pan al Ajo (x4)', precio=8.00)
    pQueso2 = Producto(comida='Palitos de Queso (x2)', precio=5.50)
    pQueso4 = Producto(comida='Palitos de Queso (x4)', precio=11.00)

    # Pizzas
    PHf = Producto(comida='Pizza Hawaiana Familiar', precio=32.90)
    PHg = Producto(comida='Pizza Hawaiana Grande', precio=22.90)
    PHm = Producto(comida='Pizza Hawaiana Mediana', precio=16.90)
    PHp = Producto(comida='Pizza Hawaiana Personal', precio=10.00)
    PAf = Producto(comida='Pizza Americana Familiar', precio=29.90)
    PAg = Producto(comida='Pizza Americana Grande', precio=19.90)
    PAm = Producto(comida='Pizza Americana Mediana', precio=13.90)
    PAp = Producto(comida='Pizza Americana Personal', precio=7.00)
    PPf = Producto(comida='Pizza de Pepperoni Familiar', precio=30.90)
    PPg = Producto(comida='Pizza de Pepperoni Grande', precio=20.90)
    PPm = Producto(comida='Pizza de Pepperoni Mediana', precio=14.90)
    PPp = Producto(comida='Pizza de Pepperoni Personal', precio=8.00)
    PMf = Producto(comida='Pizza Mozarella Familiar', precio=31.90)
    PMg = Producto(comida='Pizza Mozarella Grande', precio=21.90)
    PMm = Producto(comida='Pizza Mozarella Mediana', precio=15.90)
    PMp = Producto(comida='Pizza Mozarella Personal', precio=9.00)

    # Bebidas
    CPersonal = Producto(comida='Coca Cola Personal', precio=2.50)
    InP = Producto(comida='Inca Kola Personal', precio=2.50)
    FaP = Producto(comida='Fanta Personal', precio=3.20)
    SpP = Producto(comida='Sprite Personal', precio=3.20)

    db = SQLAlchemy(app)

    if len(Producto.query.all()) == 0:
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
        
        user = Usuario.query.filter(Usuario.usuario == username).first()
        if user is None:
            abort(403)
        else:
            if user.verify_password(password):
                ped= Pedido(user_id=user.id)
                ped_id= ped.insert()
                return jsonify({
                    'success': True,
                    'profile': {
                        'usuario': username
                    },
                    'pedido_id':ped_id
                })
            else:
                abort(403)
    

    @app.route('/users', methods = ['POST']) #registro de usuario - POST
    def insert_users():
        username = request.get_json()['username']
        password = request.get_json()['password']
        nombre = request.get_json()['name'] 
        apellido = request.get_json()['lastname']       
        email = request.get_json()['email']
        direccion = request.get_json()['address']
        telefono = request.get_json()['phone']

        print(nombre)

        if nombre is '':
            abort(403)
        else:
            user_base = Usuario.query.filter_by(usuario=username).first()
            email_base = Usuario.query.filter_by(email=email).first()

            if user_base is None and email_base is None:
                user = Usuario(usuario=username,contrasena=password,nombre=nombre,apellido=apellido,email=email,direccion=direccion,telefono=telefono)
                new_user_id= user.insert()
                selection= Usuario.query.order_by('id').all()
                current_users= [user.format() for user in selection]

                return jsonify({
                    'success':True,
                    'created':new_user_id,
                    'usuarios': current_users,
                    'total_usuarios': len(selection)
                })
            else: 
                if user_base.username == username or email_base.email == email:
                    abort(403)

    @app.route('/cart', methods=['POST'])
    def fill_cart():
        ped_id = request.get_json()['pedidoID']

        select= DetallesPedido.query.filter(DetallesPedido.pedido_id == ped_id)
        detalles= [det.format() for det in select]
        productos= [prod.detalles0.format() for prod in select]

        return jsonify({
            'success':True,
            'detalles': detalles,
            'productos':productos,
        })
    
    @app.route('/details', methods=['POST'])
    def insert_details():
        pedido_id = request.get_json()['pedidoID']
        producto_id = request.get_json()['productoID']
        
        detail = DetallesPedido(pedido_id=pedido_id,producto_id=producto_id)
        new_detai_id= detail.insert()

        return jsonify({
            'success': True,
            'created': new_detai_id
        })
    
    @app.route('/details/<detail_id>',methods=['DELETE'])
    def delete_detail(detail_id):

        todo= DetallesPedido.query.filter(DetallesPedido.id==detail_id).one_or_none()
        if todo is None:
            abort(404)
        
        todo.delete()

        return jsonify({
            'success': True,
            'deleted': detail_id,
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
