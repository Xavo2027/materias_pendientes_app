from flask import Blueprint, render_template, request, redirect, url_for, flash, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email == 'admin@example.com' and password == 'admin':
            session['usuario'] = email
            return redirect(url_for('home'))
        else:
            flash('Credenciales incorrectas', 'danger')
    return render_template('login.html')
