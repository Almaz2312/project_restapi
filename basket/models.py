from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Basket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.customer} /n {self.product} /n Total - {self.total_price}'
