from flask import Flask, render_template, redirect, url_for, session
from flask_login import LoginManager
from config import Config

from routes.auth import auth_bp
from routes.coordinador import coordinador_bp
from routes.administrativo import admin_bp
from routes.ceo import ceo_bp
from routes.alumnos import alumnos_bp

app = Flask(__name__)
app.config.from_object(Config)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(coordinador_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(ceo_bp)
app.register_blueprint(alumnos_bp)

@app.route('/')
def home():
    if "usuario" not in session:
        return redirect(url_for('auth.login'))
    return "Bienvenido a la Gestión de Materias Pendientes"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
