from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.books_views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]