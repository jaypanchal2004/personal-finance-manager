import unittest
from app import app, db
from models import User

class AuthTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register(self):
        response = self.app.post('/register', data=dict(username='testuser', email='test@example.com', password='password'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('Registration successful!', response.data.decode())

    def test_login(self):
        self.app.post('/register', data=dict(username='testuser', email='test@example.com', password='password'))
        response = self.app.post('/login', data=dict(username='testuser', password='password'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('Login successful!', response.data.decode())

if __name__ == '__main__':
    unittest.main()
