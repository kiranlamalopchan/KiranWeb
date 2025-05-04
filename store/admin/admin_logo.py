from django.contrib import admin
from store.models import Logo


@admin.register(Logo)
class AdminLogo(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']
