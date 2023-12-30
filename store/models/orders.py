from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Orders(models.Model):
    order_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_qty = models.IntegerField(default=1)
    order_price = models.IntegerField()
    order_address = models.CharField(max_length=100, default='', blank=True)
    order_mobile = models.CharField(max_length=10, default='', blank=True)
    order_date = models.DateField(default=datetime.datetime.today)
    order_status = models.BooleanField(default=False)

    # def __str__(self) -> str:
    #     return self.order_customer

    @staticmethod
    def get_orders_by_customer(customerId):
        # we can separate line with help of \
        return Orders.objects.filter(order_customer = customerId)