from django.db import models


class Subcategory(models.Model):
    subcategory = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.subcategory

    @staticmethod
    def get_all_subcategory():
        return Subcategory.objects.all()
