from django.shortcuts import render, redirect
from store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
import razorpay
from django.views.decorators.csrf import csrf_exempt


def email(request):
    return render(request, 'email_template.html')


class Cart(View):
    def get(self, request):
        ids = list(request.session.get('cart').keys())
        val = list(request.session.get('cart').values())
        print("vals",val)
        products = Product.get_products_by_id(ids)
        print(products)
        prod_list = list(products)
        print("Product List :",prod_list)
        print("Customer ID", request.session.get('customer'))
        return render(request, 'cart.html', {'products': products})


