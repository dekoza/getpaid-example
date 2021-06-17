from django.db import models

# Create your models here.
from getpaid.models import AbstractOrder


class MyCustomModel(AbstractOrder):
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    description = models.CharField(max_length=128)

    # def get_absolute_url(self):
    #     return reverse('order-detail', kwargs={"pk": self.pk})

    def get_total_amount(self):
        return self.amount

    def get_buyer_info(self):
        return {"email": self.buyer.email}

    def get_currency(self):
        return "EUR"

    def get_description(self):
        return self.description


class DummyModel(models.Model):
    dummy = models.TextField()
