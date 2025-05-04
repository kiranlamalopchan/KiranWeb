from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customers import Customer
from store.models import Mac, Ipad, IPhone, Beatsbydre, Applecare, Appleaccessories, Bose, Payment

# --------- LOGIN VIEW ----------
class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        context = {
            'macs': Mac.get_all_maclist(),
            'ipads': Ipad.get_all_ipadlist(),
            'iphones': IPhone.get_all_iPhonelist(),
            'beats': Beatsbydre.get_all_beatsbydrelist(),
            'applecares': Applecare.get_all_applecarelist(),
            'accessories': Appleaccessories.get_all_appleaccessorieslist(),
            'bose': Bose.get_all_boselist(),
            'payments': Payment.get_all_payment(),
        }
        return render(request, 'login.html', context)

    def post(self, request):
        username = request.POST.get('uname')
        password = request.POST.get('upass')
        ob_customer = Customer.get_customer_by_username(username)
        values = {'username': username}

        if ob_customer and check_password(password, ob_customer.password):
            request.session['userid'] = ob_customer.id
            request.session['username'] = ob_customer.username

            if Login.return_url:
                return HttpResponseRedirect(Login.return_url)
            else:
                Login.return_url = None
                return redirect('home')
        else:
            errmsg = "Username and Password didn't match."

        context = {
            'errmsg': errmsg,
            'values': values,
            'macs': Mac.get_all_maclist(),
            'ipads': Ipad.get_all_ipadlist(),
            'iphones': IPhone.get_all_iPhonelist(),
            'beats': Beatsbydre.get_all_beatsbydrelist(),
            'applecares': Applecare.get_all_applecarelist(),
            'accessories': Appleaccessories.get_all_appleaccessorieslist(),
            'bose': Bose.get_all_boselist(),
            'payments': Payment.get_all_payment(),
        }
        return render(request, 'login.html', context)