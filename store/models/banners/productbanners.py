from django.db import models
from store.models.categories.subcategory import Subcategory


class Productbanner(models.Model):
    title = models.CharField(max_length=500)
    product_subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default='1')
    image = models.ImageField(upload_to='uploads/banners/productbanners', null=True)

    def __str__(self):
        return self.title

    @staticmethod
    def get_productbanner_bysubcategory(subcategoryid):
        return Productbanner.objects.filter(product_subcategory_id=subcategoryid)
