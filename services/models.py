from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.ImageField(upload_to='services', blank=True)
    info = models.TextField()

    def __str__(self):
        return self.name


class ServiceItem(models.Model):
    service = models.ForeignKey('Service', related_name='service_items', on_delete=models.CASCADE)
    item_info = models.CharField(max_length=255)
