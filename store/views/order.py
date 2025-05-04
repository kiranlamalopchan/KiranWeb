from django.shortcuts import render
from django.views import View
from store.models import Mac, Ipad, Bose, Beatsbydre, Applecare, IPhone, Appleaccessories, Payment, Order, Product, \
    Customer


class OrderView(View):
    def get(self, request):
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

        userid = request.session.get('userid')
        orders = Order.get_order_userId(userid)

        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'bose': bose,
                   'payments': payments, 'orders': orders}
        return render(request, 'order.html', context)

