from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe

from photographer_portfolio.utils import delete_image_from_s3


class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='blog_media')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')


@receiver(pre_delete, sender=Post)
def delete_image_of_model_category(sender, instance, **kwargs):
    delete_image_from_s3(instance, 'image')
