from django.core.management.base import BaseCommand
from seminar2_app.models import Client

class Command(BaseCommand):
    help = "Create client"

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="User Name")
        parser.add_argument('email', type=str, help="User Email")
        parser.add_argument('phone_number', type=str, help="User phone number")
        parser.add_argument('adress', type=str, help="User adress")

    def handle(self, *args, **kwargs):
        name, email, phone_number, adress = kwargs.get('name'), kwargs.get('email'), kwargs.get('phone_number'), kwargs.get('adress')
        client = Client(name=name.capitalize(), email=email, phone_number=phone_number, adress=adress)
        client.save()
        self.stdout.write(f'Added new client!\n{client}')