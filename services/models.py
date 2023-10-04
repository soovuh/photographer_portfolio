from django.db import models
from django.utils.safestring import mark_safe


class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='services', blank=True)
    info = models.TextField()

    def __str__(self):
        return self.name

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')


class ServiceItem(models.Model):
    service = models.ForeignKey('Service', related_name='service_items', on_delete=models.CASCADE)
    item_info = models.CharField(max_length=255)
