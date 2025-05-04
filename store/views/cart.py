from django.views import View
from django.shortcuts import render
from store.models import Mac, Ipad, IPhone, Beatsbydre, Applecare, Appleaccessories, Bose, Payment
from store.models import Product


class Cart(View):
    @staticmethod
    def get(request):
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

        cart = request.session.get('cart')
        if cart:
            ids = list(request.session.get('cart').keys())
            products = Product.get_product_cart_id(ids)
        else:
            message = "Your Shopping Cart is Empty!"
            context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                       'applecares': applecares, 'accessories': appleaccessories, 'bose': bose,
                       'payments': payments, 'message': message}
            return render(request, 'cart.html', context)

        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'bose': bose,
                   'payments': payments, 'products': products}
        return render(request, 'cart.html', context)
