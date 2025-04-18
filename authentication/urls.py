from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . import views

# urlpatterns = [

#     path('login/', LoginPageView.as_view(), name='login'),
#     path('logout/', LogOutView.as_view(), name='logout'),
#     path('register/', RegisterPageView.as_view(), name='register'),

#     path('password_change/', auth_views.PasswordChangeView.as_view(template_name='authentication/password_change.html'), name='password_change'),
#     path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(template_name='authentication/password_change_done.html'), name='password_change_done'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(template_name='authentication/password_reset.html'), name='password_reset'),
#     path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='authentication/password_reset_done.html'), name='password_reset_done'),
#     path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='auth/password_reset_confirm.html'), name='password_reset_confirm'),
#     path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='authentication/password_reset_complete.html'), name='password_reset_complete'),

# ]


urlpatterns = [

    path('registration/', views.UserRegistrationView.as_view(), name='registration'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name='reset_password_request'),
    path('password_reset_complete/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(), name='reset_password_confirm'),
]

