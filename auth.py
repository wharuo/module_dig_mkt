from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
import json
from models.user import User

auth_bp = Blueprint('auth', __name__)

bcrypt = Bcrypt()

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('auth.register'))
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        with open('users.json', 'r') as f:
            users = json.load(f)
        user_id = str(len(users) + 1)
        users[user_id] = {'username': username, 'password': hashed_password}
        with open('users.json', 'w') as f:
            json.dump(users, f)
        flash('Registration successful')
        return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        with open('users.json', 'r') as f:
            users = json.load(f)
        for user_id, user_info in users.items():
            if user_info['username'] == username and bcrypt.check_password_hash(user_info['password'], password):
                user = User(id=user_id, username=username)
                login_user(user)
                return redirect(url_for('dashboard.index'))
        flash('Invalid credentials')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
