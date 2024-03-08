from django.contrib import admin
from .models import Client, Product, Order

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone_number', 'adress', 'sign_up_date']
    list_filter = ['sign_up_date']
    search_fields = ['name', 'email', 'phone_number', 'adress']

    readonly_fields = ['sign_up_date']
    fieldsets = [
        (
        None,
        {
            'classes': ['wide'],
            'fields': ['name'],
        },
    ),
    (
        "Персональные данные",
        {
            'classes': ['collapse'],
            'description': 'Номер телефона, адресс и почта клиента',
            'fields': ['email', 'phone_number', 'adress'],
        },
    ),
    (
        "Дата регистрации", 
        {
            'classes': ['wide'],
            'fields': ['sign_up_date'],
        }
    )]

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'quantity', 'addition_date']
    list_filter = ['addition_date']
    search_fields = ['name', 'description', 'price']
    
    readonly_fields = ['addition_date']
    fieldsets = [
        (
        None,
        {
            'classes': ['wide'],
            'fields': ['name'],
        },
    ),
    (
        "Доп. информация о продукте",
        {
            'classes': ['collapse'],
            'description': 'Описание и картинка продукта',
            'fields': ['description', 'image'],
        },
    ),
    (
        "Количество продукта на складе и его цена", 
        {
            'classes': ['collapse'],
            'fields': ['quantity', 'price'],
        }
    ),
    (
        "Дата добавления продукта",
        {
            'classes': ['wide'],
            'fields': ['addition_date'],
        }
    )]

class OrderAdmin(admin.ModelAdmin):
    list_filter = ['order_date']
    search_fields = ['client']
    list_display = ['client_name', 'products_list', 'order_sum', 'order_date']

    def client_name(self, obj):
        return obj.client.name
        
    def products_list(self, obj):
        return ', '.join([product.name for product in obj.products.all()])

    def client_email(self, obj):
        return obj.client.email

    def client_phone_number(self, obj):
        return obj.client.phone_number

    def client_adress(self, obj):
        return obj.client.adress
    
    fieldsets = [
        (
        'Персональные данные клиента', 
        {
            'description': 'Имя, почта, номер телефона и адресс клиента',
            'fields': ['client_name', 'client_email', 'client_phone_number', 'client_adress'],
        }
    ),
    (
        'Продукты', 
        {
            'classes': ['collapse'],
            'fields': ['products'],
        }
    ),
    (
        'Информация о заказе', 
        {
            'description': 'Дата заказа и его сумма',
            'fields': ['order_sum', 'order_date'],
        }
    )]

    readonly_fields = ['client_name', 'client_email', 'client_phone_number', 'client_adress', 'order_date']

admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
