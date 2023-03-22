from django.urls import path
from . import views

urlpatterns = [
    path('aboutus/', views.aboutus, name = 'aboutus'),
    path('contact/', views.contact, name = 'contact'),    
    path('blog/', views.blog, name = 'blog'),
    path('error/', views.error, name = 'error'),
]