from flask import Flask, render_template, redirect, url_for, session
from flask_login import LoginManager
from config import Config
import os

from routes.auth import auth_bp
from routes.alumnos import alumnos_bp

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

# Solución: user_loader vacío para que Flask-Login no rompa
@login_manager.user_loader
def load_user(user_id):
    return None  # No se cargan usuarios desde la base, solo usamos session

app.register_blueprint(auth_bp)
app.register_blueprint(alumnos_bp)

@app.route('/')
def home():
    if "usuario" not in session:
        return redirect(url_for('auth.login'))
    return "Bienvenido a la Gestión de Materias Pendientes"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
