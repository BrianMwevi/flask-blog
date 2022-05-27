from flask import render_template, redirect, url_for, request
from flask_login import login_required
from app.urls import user
from app.models import User, Article
from app import photos
from sqlalchemy import desc
import os


@user.route('/profile/<int:user_id>', methods=['GET', 'POST'])
@login_required
def profile(user_id):
    articles = Article.query.order_by(
        desc('created_at')).filter_by(author_id=user_id).all()
    return render_template('profile.html', articles=articles)
