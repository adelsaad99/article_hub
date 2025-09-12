from django.urls import path
from . import views

urlpatterns = [
  # Home page showing latest articles
  path('', views.home, name='home'),

  # Detailed view of a single article
  path('article/<int:article_id>/', views.article_detail, name='article_detail'),

  # Create a new article
  path('article/create/', views.create_article, name='create_article'),

  # Edit an existing article by ID
  path('article/edit/<int:article_id>/', views.edit_article, name='edit_article'),

  # Delete an existing article by ID
  path('article/delete/<int:article_id>/', views.delete_article, name='delete_article'),

  # Contact page to send messages
  path('contact/', views.contact, name='contact'),
]
