from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField()
    phone_number = models.CharField(max_length=16)
    adress = models.CharField(max_length=100)
    sign_up_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Name: {self.name}, email: {self.email}, phone number: {self.phone_number}, adress: {self.adress}, registration date: {self.sign_up_date}"

class Product(models.Model):
    name = models.CharField(max_length=42)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    addition_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='product_photos/', null=True, blank=True)

    def __str__(self):
        return f"Name: {self.name}, description: {self.description}, price: {self.price}, quantity: {self.quantity}, addition date: {self.addition_date}"

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_sum = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Client: {self.client.name}, sum of order: {self.order_sum}, order date: {self.order_date}"