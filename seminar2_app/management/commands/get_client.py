from django.core.management.base import BaseCommand
from seminar2_app.models import Client

class Command(BaseCommand):
    help = "Get client by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help="Client ID")

    def handle(self, *args, **kwargs):
        client_id = kwargs.get('pk')
        client = Client.objects.filter(pk=client_id).first()
        self.stdout.write(f"{client}")