from django.contrib import admin
from blog.models import Post
from modeltranslation.admin import TranslationAdmin


@admin.register(Post)
class PostAdmin(TranslationAdmin):
    readonly_fields = ['img_preview']
