from django.contrib import admin

from portfolio.models import Photo, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
