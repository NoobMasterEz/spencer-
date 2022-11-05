from datetime import date

from django.db import models

# Create your models here.


class Camera(models.Model):
    name = models.CharField(max_length=30)
    ip = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class ImageTransaction(models.Model):
    output_base64 = models.CharField(max_length=100000)
    origin_base64 = models.CharField(max_length=100000)
    create_date = models.DateField(default=date.today)
    camera = models.ForeignKey(
        Camera,
        on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"


class Centroids(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    image_transaction = models.ForeignKey(
        ImageTransaction,
        on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
