from django.contrib import admin
from django.contrib.admin import ModelAdmin

from goods.models import Good, Category, Images


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass


@admin.register(Images)
class ImagesAdmin(ModelAdmin):
    list_display = ['id', 'good']


@admin.register(Good)
class GoodAdmin(ModelAdmin):
    list_display = ['id', 'name']
