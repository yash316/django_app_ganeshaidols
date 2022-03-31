from django.contrib import admin
from django.urls import path, include
from .views import home, shop, login, signup, cart, order, checkout
from .views.checkout import CheckOut, email
from .middlewares.auth import auth_middleware

urlpatterns = [
    path('', home.index, name='Home'),
    path('shop/', shop.Shop.as_view(), name='Shop'),
    path('signup/', signup.Signup.as_view(), name='SignUp'),
    path('login/', login.Login.as_view(), name='Login'),
    path('about-us/', home.about, name='About'),
    path('contact-us/', home.contact, name='Contact'),
    path('logout/', login.logout, name='Logout'),
    path('cart/', cart.Cart.as_view(), name='Cart'),
    path('email/',checkout.email, name='Email'),
    path('check-out/', auth_middleware(CheckOut.as_view()), name='Checkout'),
    path('orders/', auth_middleware(order.OrderView.as_view()), name='Orders'),
    # path('success/', cart.success, name='Success')

]
