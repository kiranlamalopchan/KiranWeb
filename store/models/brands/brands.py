from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/brands/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_brands():
        return Brand.objects.all()