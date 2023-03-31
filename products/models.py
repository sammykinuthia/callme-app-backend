from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/images')
    owner = models.ForeignKey(User, related_name='product', on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name