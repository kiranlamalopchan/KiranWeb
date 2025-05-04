from django.db import models
from store.models.categories.subcategory import Subcategory


class Ipad(models.Model):
    name = models.CharField(max_length=500)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_ipadlist():
        return Ipad.objects.all()
