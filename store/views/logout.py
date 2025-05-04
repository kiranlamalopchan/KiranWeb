from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout


class Logout(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('home')
