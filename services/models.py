from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe

from photographer_portfolio.utils import delete_image_from_s3


class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='services', blank=True)
    info = models.TextField()

    def __str__(self):
        return self.name

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')


@receiver(pre_delete, sender=Service)
def delete_image_of_model_category(sender, instance, **kwargs):
    delete_image_from_s3(instance, 'image')


class ServiceItem(models.Model):
    service = models.ForeignKey('Service', related_name='service_items', on_delete=models.CASCADE)
    item_info = models.CharField(max_length=255)
