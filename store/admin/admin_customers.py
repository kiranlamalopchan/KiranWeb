from django.contrib import admin
from store.models import Customer


@admin.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ['username', 'password', 'email', 'mobilenumber', 'address', 'city', 'country', 'zip', 'agree_terms']
