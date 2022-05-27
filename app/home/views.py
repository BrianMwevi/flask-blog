from flask import render_template
from app.models import Article
from app.urls import home
from app.quotes.requests import get_quotes


# Homepage View
@home.route('/')
def index():
    articles = Article.query.all()
    quote = get_quotes()
    return render_template('index.html', articles=articles, quote=quote)
