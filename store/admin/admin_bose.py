from django.contrib import admin
from store.models import Bose


@admin.register(Bose)
class AdminBose(admin.ModelAdmin):
    list_display = ['id', 'name']

