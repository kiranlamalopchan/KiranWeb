from django.views import View
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
from store.models import Banner, Payment, Section, Brand, Product, Mac, Ipad, IPhone, Beatsbydre, Applecare, \
    Appleaccessories, Bose, Logo


class Homeview(View):
    @staticmethod
    def get(request):
        # Handle AJAX request to load more products
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            offset = int(request.GET.get('offset', 0))
            limit = int(request.GET.get('limit', 8))
            more_products = Product.get_all_products()[offset:offset + limit]
            data = serializers.serialize('json', more_products)
            return JsonResponse({'products': data})

        # Load initial content
        context = {
            'macs': Mac.get_all_maclist(),
            'ipads': Ipad.get_all_ipadlist(),
            'iphones': IPhone.get_all_iPhonelist(),
            'beats': Beatsbydre.get_all_beatsbydrelist(),
            'applecares': Applecare.get_all_applecarelist(),
            'accessories': Appleaccessories.get_all_appleaccessorieslist(),
            'bose': Bose.get_all_boselist(),
            'banners': Banner.get_all_banners(),
            'sections': Section.get_section_detail(),
            'brands': Brand.get_all_brands(),
            'products': Product.get_all_products().order_by('?')[:8],
            'payments': Payment.get_all_payment(),
            'logo': Logo.get_logo(),
            'initial_limit': 8,
            'media_url': settings.MEDIA_URL  # ✅ Add this line

        }

        return render(request, 'home.html', context)