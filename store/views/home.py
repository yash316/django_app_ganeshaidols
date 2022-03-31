from django.shortcuts import render, redirect
from store.models.contactRequests import Contact_Request


def index(request):
    print('user email', request.session.get('email'))
    return render(request, 'index.html')


def about(request):
    return render(request, 'aboutus.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contactrequest = Contact_Request(name=name,
                              email=email,
                              phone=phone,
                              message=message)
        contactrequest.save()


    return render(request, 'contactus.html')
