from django.core.management.base import BaseCommand
from seminar2_app.models import Product

class Command(BaseCommand):
    help = "Create product"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="product name")
        parser.add_argument('description', type=str, help="product description")
        parser.add_argument('price', type=int, help="product price")
        parser.add_argument('quantity', type=int, help="product quantity")

    def handle(self, *args, **kwargs):
        name, description, price, quantity = kwargs.get('name'), kwargs.get('description'), kwargs.get('price'), kwargs.get('quantity')
        product = Product(name=name, description=description, price=price, quantity=quantity)
        product.save()
        self.stdout.write(f"Added new product\n{product}")