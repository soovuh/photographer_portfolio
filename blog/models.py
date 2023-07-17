from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='blog_media')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
