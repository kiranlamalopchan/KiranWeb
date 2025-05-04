from django.contrib import admin
from store.models import Category, Subcategory, MainCategory


@admin.register(MainCategory)
class AdminMainCategory(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['id', 'name', 'maincategory_id', 'maincategory']


@admin.register(Subcategory)
class AdminSubcategory(admin.ModelAdmin):
    list_display = ['id', 'subcategory']
