from django.contrib import admin
from django import forms
from services.models import ServiceItem, Service


class CustomTextarea(forms.Textarea):
    def __init__(self, attrs=None):
        default_attrs = {'cols': '80', 'rows': '3'}  # Customize width and height here
        if attrs:
            default_attrs.update(attrs)
        super().__init__(default_attrs)


class ServiceItemForm(forms.ModelForm):
    class Meta:
        model = ServiceItem
        fields = '__all__'
        widgets = {
            'item_info': CustomTextarea(),  # Use the custom widget for item_info field
        }


class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    form = ServiceItemForm


@admin.register(Service)
class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['img_preview']
    inlines = [ServiceItemInline]
