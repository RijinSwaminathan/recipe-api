from django.contrib.auth import get_user_model
from django.test import TestCase


class TestModel(TestCase):
    def test_create_user_using_email_id(self):
        """Test for creating the  user  using the email_id"""

        email = 'test@untanglestrategy.com'
        password = 'Untangle@321'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password), password)

    def test_user_email_with_normalized_mail(self):
        """Test for creating the user with normalized_email"""

        email = 'test@UNTANGLESTRATEGY.COM'
        user = get_user_model().objects.create_user(email=email, password='test123')

        self.assertEqual(user.email, email.lower())

    def test_user_email_value(self):
        """Test to check the value of user email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None, password='test123')

    def test_create_super_user(self):
        """Test to check the super user is created"""
        email = 'test@Unatanglestrategy.com'
        password = 'test123'
        user = get_user_model().objects.create_superuser(email=email, password=password)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
