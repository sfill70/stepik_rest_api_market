from django.db import models
from django.contrib.auth.models import User


class ProductSets(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    description = models.TextField(verbose_name="description")

    def __str__(self):
        return self.title
