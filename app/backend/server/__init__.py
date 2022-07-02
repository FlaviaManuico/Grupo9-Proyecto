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
