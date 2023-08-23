from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('gallery/', views.gallery, name='gallery'),
    path('artist/', views.artist, name='artist'),
    path('contact/', views.contact, name='contact'),
    path('book/', views.book, name='book'),
    path('login/', views.login, name='login'),
    path('dashboard/<str:pk>/', views.client, name="customer"),
    path('dashboard-artist/', views.dashboard, name='dashboard'),
]