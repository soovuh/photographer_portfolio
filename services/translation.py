from modeltranslation.translator import register, TranslationOptions
from .models import Service, ServiceItem


@register(Service)
class PostTranslationOptions(TranslationOptions):
    fields = ('name', 'info')


@register(ServiceItem)
class PostTranslationOptions(TranslationOptions):
    fields = ('item_info',)


