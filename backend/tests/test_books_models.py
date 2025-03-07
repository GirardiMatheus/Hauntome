from django.test import TestCase
from django.contrib.auth import get_user_model
from books.models import Book

User = get_user_model()

class BookModelTest(TestCase):
    def test_create_book(self):
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='Test Description',
            user=user
        )
        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, 'Test Author')
        self.assertEqual(book.user, user)