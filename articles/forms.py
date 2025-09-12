from django import forms
from .models import Article, ContactMessage

# Form for creating and editing articles
class ArticleForm(forms.ModelForm):
  class Meta:
    model = Article
    fields = ['title', 'content', 'category', 'image']
    widgets = {
      'title': forms.TextInput(attrs={'class': 'form-control'}),         # Input for title
      'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),  # Text area for content
      'category': forms.Select(attrs={'class': 'form-control'}),          # Dropdown for category
    }

# Form for contact messages
class ContactForm(forms.ModelForm):
  class Meta:
    model = ContactMessage
    fields = ['full_name', 'email', 'message']
    widgets = {
      'full_name': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Full Name'
      }),
      'email': forms.EmailInput(attrs={
        'class': 'form-control', 
        'placeholder': 'Your Email Address'
      }),
      'message': forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message',
        'rows': 5
      }),
    }
  
  # Make all fields required
  def __init__(self, *args, **kwargs):
    super(ContactForm, self).__init__(*args, **kwargs)
    for field in self.fields:
      self.fields[field].required = True
