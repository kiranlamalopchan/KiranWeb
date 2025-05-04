from django.views import View
from django.shortcuts import render
from store.models.allproducts.products import Product
from store.models import Mac, Payment, Productbanner, Ipad, IPhone, Beatsbydre, Applecare, Appleaccessories, Bose
from store.models.categories import Category


class Productview(View):
    @staticmethod
    def get_product_nav(request, my_id):
        # -------- Nav link List ------
        macs = Mac.get_all_maclist()
        ipads = Ipad.get_all_ipadlist()
        iphones = IPhone.get_all_iPhonelist()
        beats = Beatsbydre.get_all_beatsbydrelist()
        applecares = Applecare.get_all_applecarelist()
        appleaccessories = Appleaccessories.get_all_appleaccessorieslist()
        bose = Bose.get_all_boselist()
        # -------- Nav link List End------

        products = Product.get_all_products()
        productbanners = Productbanner.get_productbanner_bysubcategory(my_id)
        products_subcategories = Product.get_all_products_by_subcategoryID(my_id)
        productview = Product.get_productdetail_byproductID(request.GET.get('productId'))

        #  ------- filtering ---------
        applecategories = Category.get_appleCategoryList()
        payments = Payment.get_all_payment()
        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories, 'productbanners': productbanners,
                   'applecategories': applecategories, 'bose': bose, 'products_subcategories': products_subcategories,
                   'payments': payments, 'products': products,
                   }
        return render(request, 'products.html', context)

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

        #  ------- filtering ---------
        products = Product.get_all_products()
        productview = Product.get_productdetail_byproductID(request.GET.get('productId'))
        applecategories = Category.get_appleCategoryList()
        categoryId = request.GET.get('categoryId')
        subcategoryId = request.GET.get('subcategoryId')
        products_category = Product.get_all_products_by_categoryID(categoryId)
        products_subcategory = Product.get_all_products_by_subcategoryID(subcategoryId)
        payments = Payment.get_all_payment()
        if productview:
            context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                       'applecares': applecares, 'accessories': appleaccessories, 'payments': payments,
                       'productviews': productview
                       }
            return render(request, 'productdetail.html', context)

        context = {'macs': macs, 'ipads': ipads, 'iphones': iphones, 'beats': beats,
                   'applecares': applecares, 'accessories': appleaccessories,
                   'applecategories': applecategories, 'bose': bose, 'products': products, 'payments': payments,
                   'products_categories': products_category, 'products_subcategories': products_subcategory,
                   }
        return render(request, 'products.html', context)

    def post(self, request):
        product_detail = Product.get_productdetail_byproductID(request.POST.get('productId'))
        context = {'product_details': product_detail}
        return render(request, 'productdetail.html', context)
