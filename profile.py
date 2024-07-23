from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_bcrypt import Bcrypt
import json

profile_bp = Blueprint('profile', __name__)

bcrypt = Bcrypt()

@profile_bp.route('/dashboard/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        new_username = request.form['new_username']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        if new_password != confirm_password:
            flash('Passwords do not match')
            return redirect(url_for('profile.profile'))
        hashed_password = bcrypt.generate_password_hash(new_password).decode('utf-8')
        with open('users.json', 'r') as f:
            users = json.load(f)
        users[current_user.id]['username'] = new_username
        users[current_user.id]['password'] = hashed_password
        with open('users.json', 'w') as f:
            json.dump(users, f)
        flash('Profile updated successfully')
        return redirect(url_for('dashboard.index'))
    return render_template('profile.html', user=current_user)
