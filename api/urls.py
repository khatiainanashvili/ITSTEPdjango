from django.urls import path
from .views import BookAPIView, BookDetailAPIView, TestAPIView

urlpatterns = [
    path('test/', TestAPIView.as_view(), name='test'),
    path('', BookAPIView.as_view(), name='book-list'),
    path('book/create/', BookAPIView.as_view(), name='create-book'),
    path('book/update/<int:pk>/', BookDetailAPIView.as_view(), name='update-book'),
    path('book/delete/<int:pk>/', BookDetailAPIView.as_view(), name='delete-book'),
]
