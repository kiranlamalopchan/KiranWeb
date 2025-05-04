from django.urls import path
from .views.home import Homeview
from .views.products import Productview
from .views.signup import Signup
from .views.login import Login
from .views.logout import Logout
from .views.productdetails import ProductDetail
from .views.cart import Cart
from .views.checkout import CheckoutView
from .views.order import OrderView
from store.middleware.authmiddleware import auth_middleware

urlpatterns = [
    path('', Homeview.as_view(), name='home'),
    path('all-products/available/detail/<int:my_id>/data-render/products/', Productview.get_product_nav,
         name='product'),
    path('apple/products/', Productview.as_view(), name='apple_product'),
    path('bose/products/', Productview.as_view(), name='bose_product'),
    path('Bose-products/products/', Productview.as_view(), name='bose_products'),
    path('customers/signup/', Signup.as_view(), name='signup'),
    path('customers/login/', Login.as_view(), name='login'),
    path('customers/logout/', Logout.as_view(), name='logout'),
    path('product-details/', ProductDetail.as_view(), name='productdetail'),
    path('cart/', Cart.as_view(), name='cart'),
    path('checkout/', auth_middleware(CheckoutView.as_view()), name='checkout'),
    path('customers/order/', OrderView.as_view(), name='checkout')
]
