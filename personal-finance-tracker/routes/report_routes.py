from flask import Blueprint, render_template
from models import Transaction

report_routes = Blueprint('report_routes', __name__)

@report_routes.route('/report')
def report():
    transactions = Transaction.query.all()
    total_income = sum([t.amount for t in transactions if t.amount > 0])
    total_expenses = sum([t.amount for t in transactions if t.amount < 0])
    net_balance = total_income + total_expenses
    
    return render_template('report.html', total_income=total_income, total_expenses=total_expenses, net_balance=net_balance)
