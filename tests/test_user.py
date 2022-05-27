import unittest
from app.models import User
from app import db


class UserTest(unittest.TestCase):
    """Test case for user model"""

    def setUp(self):
        """Set up for user model instance"""
        self.user = User(email="smith@test.io",
                         username="smith", password="pass1123")

    def tearDown(self):
        """ Reset user with email smith@test.io and username smith if exists"""
        smith = User.query.filter_by(email=self.user.email).first()
        if smith:
            db.session.delete(smith)
            db.session.commit()

    def test_password_setter(self):
        """ Test password_setter test case to check password hashing and if the hashed password exists"""
        self.assertTrue(self.user.hashed_password is not None)

    def test_access_password(self):
        """ Test access password test case for checking if it raises AttributeError when trying to access the password"""
        with self.assertRaises(AttributeError):
            self.user.password

    def test_password_verification(self):
        """Test password verification to check if the hashed password can be verified"""
        self.assertTrue(self.user.verify_password('pass1123'))

    def test_delete_user(self):
        """ Test case for deleting a user """

        self.user.save()
        get_user = User.query.filter_by(email="smith@test.io").first()
        get_user.delete()
        deleted_user = User.query.filter_by(email="smith@test.io").first()
        self.assertTrue(deleted_user == None)
