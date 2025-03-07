from django.test import TestCase
from django.contrib.auth import get_user_model
from api.serializers.user_serializers import UserSerializer

User = get_user_model()

class UserSerializerTest(TestCase):
    def test_user_serializer(self):
        user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        serializer = UserSerializer(data=user_data)
        self.assertTrue(serializer.is_valid())
        user = serializer.save()
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')