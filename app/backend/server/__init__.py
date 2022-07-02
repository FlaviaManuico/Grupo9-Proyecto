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
    CORS(app, origins =['http://127.0.0.1:5000', 'http://localhost:8080'])

    @app.after_request
    def after_resquest(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorizations, true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
        return response
        
    return app