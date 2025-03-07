from django.test import TestCase
from django.contrib.auth import get_user_model
from books.models import Book
from api.serializers.books_serializers import BookSerializer

User = get_user_model()

class BookSerializerTest(TestCase):
    def test_book_serializer(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        book_data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'description': 'Test Description',
        }

        serializer = BookSerializer(data=book_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)

        book = serializer.save(user=user)  

        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.user, user)