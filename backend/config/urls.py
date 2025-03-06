from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('api.urls.api_urls')),
    path('api/', include('api.urls.book_urls')),
]