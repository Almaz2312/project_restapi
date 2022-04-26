from django.db import models
from django.contrib.auth import get_user_model

from products.models import Product

User = get_user_model()


class Comment(models.Model):
    title = models.CharField(max_length=200)
    comments = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.title}'
