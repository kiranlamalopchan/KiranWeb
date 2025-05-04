from django.contrib import admin
from django.utils.html import format_html
from store.models import Banner


@admin.register(Banner)
class AdminBanner(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="200" height="80" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['title', 'image_tag', 'banners_category', 'sub_title', ]
