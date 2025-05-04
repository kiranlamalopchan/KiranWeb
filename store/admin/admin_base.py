from django.contrib import admin
from django.utils.html import format_html
from store.models import Payment, Brand


# Register your models here.
@admin.register(Payment)
class AdminPayment(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="100" height="40" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['name', 'image_tag']


@admin.register(Brand)
class AdminBrand(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="80" height="80" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['name', 'image_tag']
