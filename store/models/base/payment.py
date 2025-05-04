from django.db import models


class Payment(models.Model):
    image = models.ImageField(upload_to='uploads/banners')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_payment():
        return Payment.objects.all()
