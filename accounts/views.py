from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from articles.models import Article

# User registration view
def register(request):
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()           # Save new user
      login(request, user)         # Log the user in
      messages.success(request, 'Registration successful!')
      return redirect('home')      # Redirect to home page
  else:
    form = UserCreationForm()      # Empty form for GET request
  return render(request, 'accounts/register.html', {'form': form})

# User login view
def login_view(request):
  if request.method == 'POST':
    form = AuthenticationForm(data=request.POST)
    if form.is_valid():
      user = form.get_user()
      login(request, user)          # Log the user in
      messages.success(request, f'Welcome back, {user.username}!')
      return redirect('home')
  else:
    form = AuthenticationForm()     # Empty form for GET request
  return render(request, 'accounts/login.html', {'form': form})

# Logout confirmation view
def logout_confirm(request):
  return render(request, 'accounts/logout.html')  # Show logout confirmation page

# User logout view
def logout_view(request):
  if request.method == 'POST':
    logout(request)                 # Log the user out
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')
  else:
    return redirect('logout_confirm')  # Redirect to confirmation if GET request

# User profile view
@login_required
def profile(request):
  user_articles = Article.objects.filter(author=request.user)  # Get articles by this user
  return render(request, 'accounts/profile.html', {'articles': user_articles})
