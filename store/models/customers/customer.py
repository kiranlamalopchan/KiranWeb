from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=500)  # Will store hashed password
    email = models.EmailField(max_length=50)
    mobilenumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    agree_terms = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    def username_exists(self):
        return Customer.objects.filter(username=self.username).exclude(id=self.id).exists()

    def signup(self):
        self.save()

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username=username)
        except Customer.DoesNotExist:
            return None
