from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Category model for articles
class Category(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
    return self.name

# Article model
class Article(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
  image = models.ImageField(upload_to='articles/', null=True, blank=True)
  created_at = models.DateTimeField(default=timezone.now)
  is_approved = models.BooleanField(default=False)
  
  def __str__(self):
    return self.title

# ContactMessage model for user messages
class ContactMessage(models.Model):
  full_name = models.CharField(max_length=100)
  email = models.EmailField()
  message = models.TextField()
  created_at = models.DateTimeField(default=timezone.now)
  is_read = models.BooleanField(default=False)
  
  def __str__(self):
    return f"Message from {self.full_name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
