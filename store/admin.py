from django.contrib import admin
from .models import Category, Product, Customer, Order, Size, Contact_Request


# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']


class AdminOrders(admin.ModelAdmin):
    list_display = ['customer', 'product', 'quantity', 'price', 'address', 'phone']


admin.site.register(Size)
admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrders)
admin.site.register(Contact_Request)