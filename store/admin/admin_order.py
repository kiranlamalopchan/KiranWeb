from django.contrib import admin
from store.models import Order


@admin.register(Order)
class AdminMac(admin.ModelAdmin):
    list_display = ['firstname', 'lastname','userid', 'email', 'product', 'address', 'quantity', 'price', 'payment']
