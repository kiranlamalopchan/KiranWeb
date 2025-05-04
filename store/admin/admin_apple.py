from django.contrib import admin
from store.models import Mac, Ipad, IPhone, Beatsbydre, Applecare, Appleaccessories


@admin.register(Mac)
class AdminMac(admin.ModelAdmin):
    list_display = ['id', 'name', 'subcategory_id']


@admin.register(Ipad)
class AdminIpad(admin.ModelAdmin):
    list_display = ['id', 'name', 'subcategory_id']


@admin.register(IPhone)
class AdminIphone(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Beatsbydre)
class AdminBeats(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Applecare)
class AdminApplecare(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Appleaccessories)
class AdminAppleaccessories(admin.ModelAdmin):
    list_display = ['id', 'name']
