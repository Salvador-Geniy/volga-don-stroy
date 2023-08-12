from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(ModelAdmin):
    pass
