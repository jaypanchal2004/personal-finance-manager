from flask import Flask, render_template, request, redirect, url_for
from routes.auth_routes import auth_bp
from routes.transaction_routes import transaction_bp
from routes.report_routes import report_bp
from routes.predict_routes import predict_bp

app = Flask(__name__)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(transaction_bp)
app.register_blueprint(report_bp)
app.register_blueprint(predict_bp)

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
