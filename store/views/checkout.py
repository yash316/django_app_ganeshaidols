from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from django.conf import settings
from store.models.product import Product
from store.models.order import Order
from django.contrib import messages
# html required modules
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class CheckOut(View):

    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
            # send_mail(
            #     'Testing',
            #     'Here is the message.',
            #     settings.EMAIL_HOST_USER,
            #     [email],
            #     # fail_silently=False,
            # )

            # send html mail
            content = ""
            html_content = render_to_string("email_template.html",
                                            {'title': 'BappaOnline', 'address': address, 'phone': phone}, )
            text_content = strip_tags(html_content)
            email_msg = EmailMultiAlternatives(
                # subject
                "Order Confirmation - BappaOnline",
                # content
                text_content,
                # from email,
                settings.EMAIL_HOST_USER,
                # rec list
                [email]
            )
            email_msg.attach_alternative(html_content, "text/html")
            email_msg.send()
            messages.success(request, 'Your Order has been placed successfully. Thank You !!')
        request.session['cart'] = {}

        return redirect('Cart')


def email(request):
    ids = list(request.session.get('cart').keys())
    val = list(request.session.get('cart').values())
    print("vals", val)
    products = Product.get_products_by_id(ids)
    print(products)
    list_for_random = range(1000000, 10000000)
    data = {}
    data['products'] = products
    data['orders_id'] = list_for_random
    return render(request, 'email_template.html', data)
