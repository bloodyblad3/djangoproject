from django.core.management.base import BaseCommand
from seminar2_app.models import Order, Client, Product

class Command(BaseCommand):
    help = "Create order"

    def add_arguments(self, parser):
        parser.add_argument('client_pk', type=int, help="Client id")
        parser.add_argument('product_pk', type=int, nargs='+', help="Product IDs")

    def handle(self, *args, **kwargs):
        client_id, product_ids = kwargs.get('client_pk'), kwargs.get('product_pk')

        client = Client.objects.filter(pk=client_id).first()
        products = Product.objects.filter(pk__in=product_ids)
        order_sum = sum(product.price for product in products)
        order = Order.objects.create(client=client, order_sum=order_sum)
        order.products.add(*products)
        self.stdout.write(f"Order created:\n{order}")