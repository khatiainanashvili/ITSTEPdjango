from django.urls import path
from .views import (
    HomeView, AddBookView, BookDetailView, 
    UpdateBookView, DeleteBookView, BuyBookView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add_book/', AddBookView.as_view(), name='add_book'), 
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('update_book/<int:pk>/', UpdateBookView.as_view(), name='update_book'),
    path('delete_book/<int:pk>/', DeleteBookView.as_view(), name='delete_book'),
    path('buy/<int:pk>/', BuyBookView.as_view(), name='buy_book'),
]
