from django.contrib import admin

from portfolio.models import Photo, Category
from modeltranslation.admin import TranslationAdmin


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    readonly_fields = ['img_preview']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
