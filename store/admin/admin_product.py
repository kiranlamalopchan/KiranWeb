from django.contrib import admin
from django.utils.html import format_html
from store.models import Product, Productbanner


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="80" height="80" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['name', 'image_tag', 'subcategory_id', 'category_id', 'maincategory', 'category', 'subcategory',
                    'price', 'specs']


@admin.register(Productbanner)
class AdminProductBanner(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="200" height="80" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['title', 'image_tag', 'product_subcategory_id', 'product_subcategory']
