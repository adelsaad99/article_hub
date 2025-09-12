from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Article, Category, ContactMessage
from .forms import ArticleForm, ContactForm

# Homepage view - shows approved articles
def home(request):
  articles = Article.objects.filter(is_approved=True).order_by('-created_at')
  return render(request, 'articles/home.html', {'articles': articles})

# Article detail view
def article_detail(request, article_id):
  article = get_object_or_404(Article, id=article_id)
  return render(request, 'articles/article_detail.html', {'article': article})

# Create article view - requires login
@login_required
def create_article(request):
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES)
    if form.is_valid():
      article = form.save(commit=False)
      article.author = request.user
      article.save()
      messages.success(request, 'Article created successfully! It will be published after admin approval.')
      return redirect('profile')
  else:
    form = ArticleForm()
  
  return render(request, 'articles/create_article.html', {'form': form})

# Edit article view - requires login
@login_required
def edit_article(request, article_id):
  # Fetch the article authored by the logged-in user
  article = get_object_or_404(Article, id=article_id, author=request.user)
  if request.method == 'POST':
    form = ArticleForm(request.POST, request.FILES, instance=article)
    if form.is_valid():
      form.save()
      messages.success(request, 'Article updated successfully!')
      return redirect('profile')
  else:
    form = ArticleForm(instance=article)
  
  return render(request, 'articles/edit_article.html', {'form': form, 'article': article})

# Delete article view - requires login
@login_required
def delete_article(request, article_id):
  # Fetch the article authored by the logged-in user
  article = get_object_or_404(Article, id=article_id, author=request.user)
  if request.method == 'POST':
    article.delete()
    messages.success(request, 'Article deleted successfully!')
    return redirect('profile')
  
  return render(request, 'articles/delete_article.html', {'article': article})

# Contact view - for sending messages to admin
def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
      return redirect('home')
    else:
      messages.error(request, 'Please correct the errors below.')
  else:
    form = ContactForm()
  
  return render(request, 'articles/contact.html', {'form': form})
