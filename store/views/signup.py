from django.shortcuts import render, redirect
from store.models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            email=email,
                            phone=phone,
                            password=password)
        # validations
        # error_message = self.validateCustomer(customer)
        if (not first_name):
            error_message = "First name is required."
        elif (not last_name):
            error_message = "Last name is required."
        elif (not phone):
            error_message = "Phone Number is required."
        elif len(phone) < 10:
            error_message = "Phone number should be of 10 digits."
        elif (not password):
            error_message = "Password is required."
        elif len(password) < 6:
            error_message = "Password should be 6 character long."
        elif (not confirm_password):
            error_message = "Confirm Password is required."
        elif (not password == confirm_password):
            error_message = "Password and Confirm Password should be same."
        elif customer.isExists():
            error_message = 'Email Address Already Exists.'
        # saving
        if not error_message:
            customer.password = make_password(customer.password)
            customer.save()
            return redirect('Home')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    # def validateCustomer(self, customer):
    #     if (not customer.first_name):
    #         error_message = "First name is required."
    #     elif (not customer.last_name):
    #         error_message = "Last name is required."
    #     elif (not customer.phone):
    #         error_message = "Phone Number is required."
    #     elif len(customer.phone) < 10:
    #         error_message = "Phone number should be of 10 digits."
    #     elif (not customer.password):
    #         error_message = "Password is required."
    #     elif len(customer.password) < 6:
    #         error_message = "Password should be 6 character long."
    #     elif customer.isExists():
    #         error_message = 'Email Address Already Exists.'
