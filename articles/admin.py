from django.contrib import admin
from .models import Article, Category, ContactMessage

# Admin configuration for Article model
class ArticleAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'is_approved', 'created_at')  # Columns shown in list
  list_filter = ('is_approved', 'category', 'created_at')           # Filters in sidebar
  search_fields = ('title', 'content', 'author__username')          # Searchable fields

# Admin configuration for ContactMessage model
class ContactMessageAdmin(admin.ModelAdmin):
  list_display = ('full_name', 'email', 'created_at', 'is_read')    # Columns shown in list
  list_filter = ('is_read', 'created_at')                            # Filters in sidebar
  search_fields = ('full_name', 'email', 'message')                  # Searchable fields
  readonly_fields = ('created_at',)                                  # Cannot edit created_at
  list_editable = ('is_read',)                                       # Editable in list view
  
  # Field groups in the admin form
  fieldsets = (
    (None, {
      'fields': ('full_name', 'email', 'message', 'is_read')
    }),
    ('Timestamps', {
      'fields': ('created_at',),
      'classes': ('collapse',)   # Collapsible section
    }),
  )

# Register models to appear in admin site
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(ContactMessage, ContactMessageAdmin)
