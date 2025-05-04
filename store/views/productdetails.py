from django.views import View
from django.shortcuts import render
from store.models.base import Payment
from store.models.allproducts import Product
from store.models.apple import Mac, Ipad, IPhone, Beatsbydre, Applecare, Appleaccessories
from store.models.bose import Bose


class ProductDetail(View):
    def get(self, request):
        products = Product.get_productdetail_byproductID(request.GET.get('productsId'))

        # -------- Nav link List ------
        macs = Mac.get_all_maclist()
        ipads = Ipad.get_all_ipadlist()
        iphones = IPhone.get_all_iPhonelist()
        beats = Beatsbydre.get_all_beatsbydrelist()
        applecares = Applecare.get_all_applecarelist()
        appleaccessories = Appleaccessories.get_all_appleaccessorieslist()
        bose = Bose.get_all_boselist()
        # -------- Nav link List End------

        payments = Payment.get_all_payment()
        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'bose': bose, 'products': products,
                   'payments': payments, }
        return render(request, 'productdetail.html', context)

    def post(self, request):
        products = Product.get_productdetail_byproductID(request.GET.get('productsId'))

        # -------- Nav link List ------
        macs = Mac.get_all_maclist()
        ipads = Ipad.get_all_ipadlist()
        iphones = IPhone.get_all_iPhonelist()
        beats = Beatsbydre.get_all_beatsbydrelist()
        applecares = Applecare.get_all_applecarelist()
        appleaccessories = Appleaccessories.get_all_appleaccessorieslist()
        bose = Bose.get_all_boselist()
        # -------- Nav link List End------

        productquantity = request.POST.get('product_quantity')
        product = request.POST.get('product')
        cart = request.session.get('cart')
        msg = " Added To Cart !"
        if cart:
            quantity = cart.get(product)
            if quantity:
                cart[product] = quantity + int(productquantity)
            else:
                cart[product] = int(productquantity)
        else:
            cart = {}
            cart[product] = int(productquantity)
        request.session['cart'] = cart
        payments = Payment.get_all_payment()
        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'bose': bose, 'products': products,
                   'payments': payments, 'message': msg}
        return render(request, 'productdetail.html', context)
