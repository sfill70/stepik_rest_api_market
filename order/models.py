from django.db import models
from django.contrib.auth.models import User
from recipient.models import Recipient
from market.models import ProductSets
from enum import Enum
from django.utils import timezone
import datetime


# class OrderChoices(models.TextChoices):
class OrderChoices(Enum):
    created = 'created'
    delivered = 'delivered'
    processed = 'processed'
    cancelled = 'cancelled'

    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]


class Order(models.Model):
    order_created_datetime = models.DateTimeField(auto_now_add=True, verbose_name="order_created")
    delivery_datetime = models.DateTimeField(verbose_name="delivery")
    delivery_address = models.CharField(max_length=200, verbose_name="address")
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE, blank=False, verbose_name="recipient")
    product_set = models.ForeignKey(ProductSets, on_delete=models.CASCADE, blank=False, verbose_name="product")
    status = models.CharField(max_length=200, choices=OrderChoices.choices(), verbose_name="status")

    def get_order_datetime(self, days):
        return self.order_created_datetime.date() == days.date()

    def __str__(self):
        return self.delivery_address + ':' + str(self.delivery_datetime)
