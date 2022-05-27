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


@user.route('/profile/<int:user_id>/update', methods=['POST'])
def update(user_id):
    user = User.query.filter_by(id=user_id).first()
    if 'photo' in request.files:
        if user.profile_pic_path:
            user_image = f"/{user.profile_pic_path.split('/')[1]}"
            path = os.path.abspath(os.environ.get(
                'UPLOADED_PHOTOS_DEST') + user_image)
            if os.path.exists(path):
                os.remove(path)

        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        user.save()
    return redirect(url_for('user.profile', user_id=user_id))
