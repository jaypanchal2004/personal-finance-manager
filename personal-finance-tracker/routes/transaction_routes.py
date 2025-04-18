from flask import Blueprint, render_template, request, redirect, url_for, flash
from models import db, Transaction

transaction_routes = Blueprint('transaction_routes', __name__)

@transaction_routes.route('/add_transaction', methods=['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        amount = request.form['amount']
        category = request.form['category']
        description = request.form['description']
        
        new_transaction = Transaction(amount=amount, category=category, description=description)
        db.session.add(new_transaction)
        db.session.commit()
        
        flash('Transaction added successfully!', 'success')
        return redirect(url_for('transaction_routes.add_transaction'))

    return render_template('add_transaction.html')

@transaction_routes.route('/transactions')
def transactions():
    transactions = Transaction.query.all()
    return render_template('transactions.html', transactions=transactions)
