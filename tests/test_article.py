import unittest
from app.models import Article, User
from app import db


class ArticleTest(unittest.TestCase):
    """Test case for Article model"""

    def setUp(self):
        """Set up for article model instance"""
        self.user = User(email="jane@test.io",
                         username="Jane", password="pass1123")
        self.article = Article(title="Sample Title",
                               category="Programming", body="Article body")

    def tearDown(self):
        """ Reset user with email jane@test.io and username Jane"""
        jane = User.query.filter_by(email=self.user.email).first()
        if jane:
            db.session.delete(jane)
            db.session.commit()

    def test_save_article(self):
        """ Test save article instance"""
        self.user.save()
        self.article.author_id = self.user.id
        articles = Article.query.all()
        self.article.save()
        self.assertTrue(len(Article.query.all()) > len(articles))

    def test_update_article(self):
        """ Test update article method """
        self.user.save()
        self.article.author_id = self.user.id
        self.article.save()
        article = Article.query.filter_by(title="Sample Title").first()
        article.title = "Updated Title"
        article.update()
        updated_article = Article.query.filter_by(
            title="Updated Title").first()
        self.assertEqual(updated_article.title, "Updated Title")

    def test_delete_article(self):
        """Test case for deleting article object"""
        self.user.save()
        self.article.author_id = self.user.id
        self.article.save()
        articles_length = len(Article.query.all())
        article = Article.query.filter_by(title="Sample Title").first()
        article.delete()
        new_articles_length = len(Article.query.all())
        self.assertTrue(articles_length > new_articles_length)
