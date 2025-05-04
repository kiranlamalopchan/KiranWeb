from django.views import View
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.hashers import make_password, check_password
from store.models.customers import Customer
from store.models import Mac, Ipad, IPhone, Beatsbydre, Applecare, Appleaccessories, Bose, Payment


# --------- SIGNUP VIEW ----------
class Signup(View):
    def validate_customer(self, customer):
        if not customer.username:
            return "Username is required."
        elif len(customer.username) < 4:
            return "Username must be at least 4 characters long."
        elif len(customer.username) > 25:
            return "Username must be less than 25 characters."
        elif customer.username_exists():
            return "Username already exists."
        elif not customer.email:
            return "Email is required."
        elif not customer.mobilenumber:
            return "Mobile number is required."
        elif len(customer.mobilenumber) != 10:
            return "Mobile number must be 10 digits."
        elif not customer.agree_terms:
            return "You must agree to the terms and conditions."
        return None

    def get_nav_context(self):
        return {
            'macs': Mac.get_all_maclist(),
            'ipads': Ipad.get_all_ipadlist(),
            'iphones': IPhone.get_all_iPhonelist(),
            'beats': Beatsbydre.get_all_beatsbydrelist(),
            'applecares': Applecare.get_all_applecarelist(),
            'accessories': Appleaccessories.get_all_appleaccessorieslist(),
            'bose': Bose.get_all_boselist(),
            'payments': Payment.get_all_payment(),
        }

    def get(self, request):
        return render(request, 'signup.html', self.get_nav_context())

    def post(self, request):
        data = request.POST
        username = data.get('uname')
        password = data.get('upass')
        email = data.get('uemail')
        mobilenumber = data.get('umobile')
        address = data.get('uaddress')
        city = data.get('ucity')
        country = data.get('ucountry')
        zip_code = data.get('uzip')
        agree_terms = 'agree_terms' in data

        customer = Customer(
            username=username,
            password=password,
            email=email,
            mobilenumber=mobilenumber,
            address=address,
            city=city,
            country=country,
            zip=zip_code,
            agree_terms=agree_terms
        )

        error = self.validate_customer(customer)
        context = self.get_nav_context()

        if not error:
            customer.password = make_password(customer.password)
            customer.signup()
            return redirect('home')
        else:
            context['errmsg'] = error
            context['values'] = {
                'username': username,
                'email': email,
                'mobilenumber': mobilenumber,
                'address': address,
                'city': city,
                'country': country,
                'zip': zip_code,
                'agree_terms': agree_terms,
            }
            return render(request, 'signup.html', context)