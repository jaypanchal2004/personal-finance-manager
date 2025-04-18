import unittest
from app import app, db
from models import Transaction

class TransactionTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_add_transaction(self):
        response = self.app.post('/add_transaction', data=dict(amount=100.0, category='Food', description='Lunch'))
        self.assertEqual(response.status_code, 302)
        transaction = Transaction.query.first()
        self.assertEqual(transaction.amount, 100.0)

if __name__ == '__main__':
    unittest.main()
