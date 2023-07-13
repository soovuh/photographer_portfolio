from django.contrib import admin

from portfolio.models import Photo, Category


@admin.register(Category)
class ShoeAdmin(admin.ModelAdmin):
    pass


@admin.register(Photo)
class ShoeAdmin(admin.ModelAdmin):
    pass
