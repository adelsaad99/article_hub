from django.urls import path
from . import views

urlpatterns = [
  # User registration page
  path('register/', views.register, name='register'),

  # User login page
  path('login/', views.login_view, name='login'),

  # Logout action
  path('logout/', views.logout_view, name='logout'),

  # Optional logout confirmation page
  path('logout/confirm/', views.logout_confirm, name='logout_confirm'),

  # User profile page
  path('profile/', views.profile, name='profile'),
]
