from django.contrib import admin
from .models import Post

# This is where you register models to include them in the Django administration site—using this site is optional.
# class PostAdmin: In this class, we can include information about how to display
# the model on the site and how to interact with it

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']