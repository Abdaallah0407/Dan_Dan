from django.db import models
from products.models import Product


class Status(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'


class Order(models.Model):
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    customer_name = models.CharField(
        max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField(
        blank=True, null=True, default=None)
    customer_phone = models.CharField(
        max_length=48, blank=True, null=True, default=None)
    customer_address = models.CharField(
        max_length=200, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_actived = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return "Заказ %s %s" % (self.id, self.is_actived.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    order = models.ForeignKey(
        Order, blank=True, null=True, default=None, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, blank=True, null=True, default=None,  on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, default=0)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return " %s" % self.product

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
