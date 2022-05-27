from flask import flash, render_template, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Subscriber
from app.urls import auth


@auth.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        user_email = User.query.filter_by(email=email).first()
        if user_email:
            flash("Email or username is already in use")
            return render_template('index.html')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, email=email, password=password)
        user.save()
        flash("Account created successfully")
        return redirect(url_for('auth.login'))
    flash("Wrong email or password. Please try again")
    return render_template('index.html')



