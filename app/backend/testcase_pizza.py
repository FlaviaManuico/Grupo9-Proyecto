import unittest
import json
import random
import string
from server import create_app
from models import setup_db, Usuario, Producto, Pedido, DetallesPedido

class TestUtecPizza(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'pizza_test'
        self.database_path='postgresql://{}:@{}/{}'.format('postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_usuario = {
            'username': ''.join(random.SystemRandom().choice(string.ascii_letters)),
            'password': 'new password',
            'name': ''.join(random.SystemRandom().choice(string.ascii_letters)),
            'lastname': ''.join(random.SystemRandom().choice(string.ascii_letters)),
            'email': ''.join(random.SystemRandom().choice(string.ascii_letters)),
            'address': ''.join(random.SystemRandom().choice(string.ascii_letters)),
            'phone': 987654321,
        }
    
    #------------------Test---------------------
    def test_create_usuario_success(self):
        # pass
        res = self.client().post('/users', json=self.new_usuario)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_usuarios'])
        self.assertTrue(len(data['usuarios']))

    def test_create_usuario_failed(self):
        pass
        # res = self.client().post('/users', json={})
        # data = json.loads(res.data)

        # self.assertEqual(res.status_code, 422)
        # self.assertEqual(data['success'], False)
        # self.assertEqual(data['message'], 'Unprocessable')

    def tearDown(self):
        pass

    