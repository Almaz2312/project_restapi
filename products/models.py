from django.db import models

from category.models import Category


class Brand(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL,
                              null=True, blank=True)
    description = models.TextField()
    size = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True, blank=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,
                                null=True, blank=True)
    image = models.ImageField(upload_to='products', default='no_photo.jpg')

    def __str__(self):
        return self.product

