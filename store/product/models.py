from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    seller = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.name
