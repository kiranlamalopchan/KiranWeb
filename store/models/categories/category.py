from django.db import models
from .maincategory import MainCategory


class Category(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    maincategory = models.ForeignKey(MainCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_categoryList():
        return Category.objects.all()

    @staticmethod
    def get_appleCategoryList():
        return Category.objects.filter(maincategory_id=1)

    @staticmethod
    def get_boseCategoryList():
        return Category.objects.filter(maincategory_id=2)

    @staticmethod
    def get_jblCategoryList():
        return Category.objects.filter(maincategory_id=3)
