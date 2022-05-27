import unittest
from app.models import Article, User, Comment
from app import db


class CommentTest(unittest.TestCase):
    """Test case for Comment model"""

    def setUp(self):
        """Set up for comment model instance"""
        self.user = User(email="john@test.io",
                         username="john", password="pass1123")
        self.article = Article(title="Article Comment",
                               category="Programming", body="Article body")
        self.comment = Comment(body="Test comment 1")

    def tearDown(self):
        """ Reset user with email john@test.io and username john"""
        john = User.query.filter_by(email=self.user.email).first()
        if john:
            db.session.delete(john)
            db.session.commit()

    def test_save_comment(self):
        """ Test save comment instance"""
        self.user.save()
        self.article.author_id = self.user.id
        self.article.save()
        comments = Comment.query.all()
        self.comment.user_id = self.user.id
        self.comment.article_id = self.article.id
        self.comment.save()
        self.assertTrue(len(Comment.query.all()) > len(comments))

    def test_update_article(self):
        """ Test update comment method """
        self.user.save()
        self.article.author_id = self.user.id
        self.article.save()
        self.comment.user_id = self.user.id
        self.comment.article_id = self.article.id
        self.comment.save()
        self.comment.body = "Updated comment body"
        self.comment.update()
        updated_comment = Comment.query.filter_by(
            body="Updated comment body").first()
        self.assertFalse(updated_comment == None)

    def test_delete_comment(self):
        """Test case for deleting a comment object"""
        self.user.save()
        self.article.author_id = self.user.id
        self.article.save()
        self.comment.user_id = self.user.id
        self.comment.article_id = self.article.id
        self.comment.save()
        saved_comment = Comment.query.filter_by(body="Test comment 1").first()
        self.assertTrue(saved_comment != None)
        saved_comment.delete()
        deleted_comment = Comment.query.filter_by(body="Test comment 1").first()
        self.assertTrue(deleted_comment == None)
