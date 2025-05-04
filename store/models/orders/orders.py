from django.db import models
from store.models import Product, Customer
import datetime


class Order(models.Model):
    firstname = models.CharField(max_length=300, default='', blank=True)
    lastname = models.CharField(max_length=300, default='', blank=True)
    email = models.EmailField(default='', blank=True)
    address = models.CharField(max_length=200, default='', blank=True)
    address_opt = models.CharField(max_length=200, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    country = models.CharField(max_length=200, default='', blank=True)
    district = models.CharField(max_length=300, default='', blank=True)
    payment = models.CharField(max_length=30, default='Cash on Delivery')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    userid = models.ForeignKey(Customer, on_delete=models.CASCADE, default='')
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    date = models.DateTimeField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    @staticmethod
    def get_order_userId(user_id):
        return Order.objects.filter(userid=user_id).order_by('-date')
