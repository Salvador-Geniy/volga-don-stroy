from django.contrib import admin
from django.contrib.admin import ModelAdmin

from goods.models import Good, Category


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']
    ordering = ['name']


@admin.register(Good)
class GoodAdmin(ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_display_links = ['id', 'name']
    search_fields = ['name']
