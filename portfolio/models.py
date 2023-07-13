from django.db import models


class Category(models.Model):
    main_image = models.ImageField(upload_to='category_images')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo_name = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio media')

    def __str__(self):
        return f'{self.photo_name} ({self.category.name})'
