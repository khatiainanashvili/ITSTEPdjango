
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('add_books', views.add_book, name='add_book'),
]