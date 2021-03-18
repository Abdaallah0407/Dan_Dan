from django.db import models
from datetime import datetime


class Categori(models.Model):
    title = models.CharField(max_length=200)
    _type = models.CharField(max_length=200)

    def __str__(self):
        return self.title
