from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.safestring import mark_safe

from photographer_portfolio.utils import delete_image_from_s3


class Review(models.Model):
    owner_name = models.CharField(max_length=255)
    owner_social = models.URLField(blank=True, null=True)
    owner_image = models.ImageField(upload_to='user_photo', blank=True)
    owner_review = models.TextField(validators=[MinLengthValidator(30), MaxLengthValidator(1000)])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.owner_name

    def img_preview(self):
        return mark_safe(f'<img src = "{self.owner_image.url}" width = "300"/>')


@receiver(pre_delete, sender=Review)
def delete_image_of_model_category(sender, instance, **kwargs):
    delete_image_from_s3(instance, 'owner_image')
