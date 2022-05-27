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


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            login_user(user)
            flash("Logged In Successfully!")
            return redirect(request.args.get('next') or url_for('home.index', category="all"))
        flash('Invalid email or password')
    return render_template('index.html')


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    flash("Logged Out Successfully!")
    return redirect(url_for('home.index'))


