from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from books.models import Book

User = get_user_model()

class BookViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_book(self):
        url = reverse('book-list')
        data = {
            'title': 'Test Book',
            'author': 'Test Author',
            'description': 'Test Description'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, 'Test Book')

    def test_list_books(self):
        Book.objects.create(
            title='Test Book',
            author='Test Author',
            description='Test Description',
            user=self.user
        )
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book')