
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),  
    path('add_books/', views.add_book, name='add_book'),
    path('book_detail/<int:id>/', views.book_details, name='book_detail'),
    path('delete_book/<int:id>/', views.delete_book, name='delete_book'),
    path('update_book/<int:id>/', views.update_book, name='update_book'),
    path('buy/<int:id>/', views.buy_book, name='buy_book'),

]





