"""
Tests for User Models
"""
from django.test import SimpleTestCase
from django.contrib.auth import get_user_model

class ModelTests(SimpleTestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):
        email='test@example.com'
        password='password123'
        user=get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Create and validate emails"""
        sample_Emails=[
            ['test1@EXAMPLE.com','test1@example.com'],
            ['TEST2@EXAMPLE.com','TEST2@example.com'],
            ['teSt3@Example.com','teSt3@example.com'],
            ['Test4@example.com','Test4@example.com']
        ]

        for email, expected in sample_Emails:
            user = get_user_model().objects().create_user(email,'sample123')
            self.assertEqual(user.email,expected)
