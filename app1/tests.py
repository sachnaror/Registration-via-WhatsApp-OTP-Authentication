
from django.test import TestCase

from .models import CustomUser


class UserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(username="testuser", password="testpass", email="test@example.com", phone_number="1234567890")

    def test_user_creation(self):
        user = CustomUser.objects.get(username="testuser")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.phone_number, "1234567890")
