from django.db import models
from store.models.categories.category import Category
from store.models.categories.subcategory import Subcategory
from store.models.categories.maincategory import MainCategory


class Product(models.Model):
    name = models.CharField(max_length=500)
    keyword = models.CharField(max_length=1000)
    specs = models.CharField(max_length=5000000, default=None, null=True, blank=True)
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=5000)
    price = models.IntegerField(default='Comming Soon')
    image = models.ImageField(upload_to=f'uploads/products/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_subcategoryID(subcategory_id):
        return Product.objects.filter(subcategory_id=subcategory_id)

    @staticmethod
    def get_all_products_by_categoryID(category_id):
        return Product.objects.filter(category_id=category_id)

    @staticmethod
    def get_productdetail_byproductID(product_id):
        return Product.objects.filter(id=product_id)

    @staticmethod
    def get_product_cart_id(ids):
        return Product.objects.filter(id__in=ids)
