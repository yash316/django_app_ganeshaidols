from django.shortcuts import render, redirect
from store.models import Product, Category, Customer,Order
from django.contrib.auth.hashers import make_password, check_password
from django.views import View
from store.middlewares.auth import auth_middleware
from django.utils.decorators import method_decorator

class OrderView(View):

    def get(self, request):
        customer = request.session.get('customer')
        orders = Order.get_orders_by_customer(customer)
        print(orders)
        return render(request, 'order.html', {'orders': orders})

