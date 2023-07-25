from modeltranslation.translator import register, TranslationOptions
from .models import Category


@register(Category)
class PostTranslationOptions(TranslationOptions):
    fields = ('name',)
