from django.contrib import admin

from portfolio.models import Photo, Category


@admin.register(Category)
class ShoeAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']


@admin.register(Photo)
class ShoeAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
