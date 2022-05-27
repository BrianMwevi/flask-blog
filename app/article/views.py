from flask import request, flash, render_template, redirect, url_for
from app.urls import article
from flask_login import login_required, current_user
from .forms import ArticleForm
from app.comment.forms import CommentForm
from app.models import Article, Subscriber
from sqlalchemy import desc, func
from datetime import date
from app import photos
from app.email.email import mail_message
from time import sleep


# All Articles
@article.route('/published/<string:category>')
@article.route('/<string:category>')
def articles(category):
    category = category.lower()
    if category == 'today':
        articles = Article.query.filter(
            func.date(Article.created_at) == date.today()).order_by(desc('created_at')).all()
    elif category == "this_week":
        articles = Article.query.order_by(desc(Article.created_at)).all()
    else:
        articles = Article.query.order_by(desc('created_at')).all()
    if request.path:
        return render_template('user_articles.html', articles=articles, category=category)
    return render_template('index.html', articles=articles)
