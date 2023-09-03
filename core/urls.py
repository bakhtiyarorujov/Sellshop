from django.urls import path
from .views import aboutus, blog, blog_detail, error, contact

urlpatterns = [
    path('aboutus/', aboutus, name='aboutus'),
    path('blog/', blog, name='blog'),
    path('blog-detail/', blog_detail, name='blog-detail'),
    path('contact/', contact, name='contact'),
    path('error/', error, name='error'),
]