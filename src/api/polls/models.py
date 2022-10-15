from django.db import models


class Rapper(models.Model):
    name = models.CharField(max_length=100)
    aka = models.CharField(max_length=60)

    def __str__(self):
        return self.aka

