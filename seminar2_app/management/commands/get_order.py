from django.core.management.base import BaseCommand
from seminar2_app.models import Order

class Command(BaseCommand):
    help = "Get order by client ID"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="order id")

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('pk')
        order = Order.objects.filter(pk=client_id).first()
        self.stdout.write(f"{order}")