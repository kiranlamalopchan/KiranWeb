from django.views import View
from django.shortcuts import render
from store.models import Mac, Ipad, IPhone, Beatsbydre, Applecare, Appleaccessories, Bose, Payment, Product, Order, \
    Customer


class CheckoutView(View):
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
            context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                       'applecares': applecares, 'accessories': appleaccessories, 'bose': bose,
                       'payments': payments}
            return render(request, 'cart.html', context)
        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'bose': bose,
                   'payments': payments, 'products': products}
        return render(request, 'checkout.html', context)

    def post(self, request):
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

        formdata = request.POST
        firstname = formdata.get('firstname')
        lastname = formdata.get('lastname')
        userid = request.session.get('userid')
        email = formdata.get('email')
        address = formdata.get('address')
        address_opt = formdata.get('addressopt')
        phoneno = formdata.get('phno')
        country = formdata.get('country')
        district = formdata.get('district')
        payment = formdata.get('paymentmethod')
        cart = request.session.get('cart')
        products = Product.get_product_cart_id(list(cart.keys()))

        for product in products:
            order = Order(firstname=firstname, lastname=lastname, email=email, address=address,
                          address_opt=address_opt,
                          phone=phoneno, country=country, district=district, payment=payment, product=product,
                          quantity=cart.get(str(product.id)), price=product.price, userid=Customer(id=userid))
            order.save()
        message = "Order Successful! , Check Status of your product in 'My Order' page. "
        request.session['cart'] = {}

        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'bose': bose,
                   'payments': payments, 'message': message}
        return render(request, 'checkout.html', context)
