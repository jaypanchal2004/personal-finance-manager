from flask import Blueprint, render_template, request
from utils.predictions import predict_finance

predict_routes = Blueprint('predict_routes', __name__)

@predict_routes.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = None
    if request.method == 'POST':
        income = float(request.form['income'])
        expenses = float(request.form['expenses'])
        prediction = predict_finance(income, expenses)
    
    return render_template('predict.html', prediction=prediction)
