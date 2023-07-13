from django.db import models
from django.utils.safestring import mark_safe


class Category(models.Model):
    main_image = models.ImageField(upload_to='category_images')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def img_preview(self):
        return mark_safe(f'<img src = "{self.main_image.url}" width = "300"/>')


class Photo(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio media')

    def __str__(self):
        return f'({self.category.name})'

    def img_preview(self):
        return mark_safe(f'<img src = "{self.image.url}" width = "300"/>')
