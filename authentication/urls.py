from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'), 
    path('logout/', views.log_out, name='logout'),
    path('register/', views.register_page, name='register'),
]
