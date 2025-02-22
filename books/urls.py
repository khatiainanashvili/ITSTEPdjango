
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('add_books/', views.add_book, name='add_book'),
    path('book_detail/<int:id>/', views.book_details, name='book_detail'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
]