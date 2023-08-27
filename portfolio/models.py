from django.db import models
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from photographer_portfolio.utils import delete_image_from_s3


class Category(models.Model):
    main_image = models.ImageField(upload_to='category_images')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def img_preview(self):
        return mark_safe(f'<img src = "{self.main_image.url}" width = "300"/>')


@receiver(pre_delete, sender=Category)
def delete_image_of_model_category(sender, instance, **kwargs):
    if not instance.has_references():
        delete_image_from_s3(instance, 'main_image')


class Photo(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio media')

    def __str__(self):
        return f'({self.category.name})'

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')


@receiver(pre_delete, sender=Photo)
def delete_image_of_model_category(sender, instance, **kwargs):
    if not instance.has_references():
        delete_image_from_s3(instance, 'image')
