from django.contrib import admin
from django.contrib.admin import ModelAdmin

from articles.models import Article


@admin.register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'created_at']

