from django.db import models
from store.models.categories.subcategory import Subcategory


class Banner(models.Model):
    image = models.ImageField(upload_to='uploads/banners')
    banners_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=7, null=True)
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=200)

    @staticmethod
    def get_all_banners():
        return Banner.objects.all()
