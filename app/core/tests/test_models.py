"""
Tests for User Models
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_user(email='user@example.com', password='testpass123'):

    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    """Test Models"""

    def test_create_user_with_email_successful(self):

        email = 'test@example.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Create and validate emails"""
        sample_Emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['TEST2@EXAMPLE.com', 'TEST2@example.com'],
            ['teSt3@Example.com', 'teSt3@example.com'],
            ['Test4@example.com', 'Test4@example.com']
        ]

        for email, expected in sample_Emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Testing the user without email raises error while validating"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):

        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )
        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample Recipe Description.',
        )

        self.assertEqual(str(recipe), recipe.title)

    def test_create_tag(self):

        user = create_user()
        tag = models.Tag.objects.create(user=user, name='Tag1')

        self.assertEqual(str(tag), tag.name)
