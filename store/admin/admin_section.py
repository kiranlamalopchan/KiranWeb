from django.contrib import admin
from django.utils.html import format_html
from store.models import Section


@admin.register(Section)
class AdminSection(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" width="80" height="60" />'.format(obj.image.url))

    image_tag.short_description = 'Image'
    list_display = ['title', 'image_tag', 'sub_title', 'description']
