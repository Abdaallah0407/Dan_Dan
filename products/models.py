from django.db import models
from datetime import datetime
from categories.models import Categori


class Product(models.Model):
    categori = models.ForeignKey(Categori, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "%s, %s" % (self.price, self.title)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
