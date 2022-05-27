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


# Add New Article
@article.route('/new', methods=['GET', 'POST'])
@login_required
def create_article():
    article_form = ArticleForm()
    if article_form.validate_on_submit():
        title = article_form.title.data
        body = article_form.body.data
        category = article_form.category.data.lower()
        article = Article(author_id=current_user.id,
                          title=title, body=body, category=category)
        if "photo" in request.files:
            filename = request.files["photo"]
            if filename:
                article.image_path = f"photos/{photos.save(filename)}"
        article.save()
        subscribers = Subscriber.query.all()
        if subscribers:
            for subscriber in subscribers:
                mail_message("Welcome to Flask Blog IO!",
                             "email/welcome_user", subscriber.email)
            sleep(0.05)
        flash("Article created successfully!")
        flash(f"Emailed {len(subscribers)} subscribers")
        return redirect(request.args.get('next') or url_for('article.articles', category=category))
    return render_template('forms/new_article.html', article_form=article_form)


# Display Article Details
@article.route('/detail/<int:article_id>/')
def detail(article_id):
    comment_form = CommentForm()
    article = Article.query.filter_by(id=article_id).first()
    return render_template('article_detail.html', article=article, comment_form=comment_form)
