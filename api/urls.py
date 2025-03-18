from django.urls import path
from . import views

urlpatterns = [
    # path('', views.test),
    path('', views.book_list),
    path('book/create/', views.create_book),
    path('book/update/<int:pk>/', views.update_book),
    path('book/delete/<int:pk>/', views.delete_book),
]