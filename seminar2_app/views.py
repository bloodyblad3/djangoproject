from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta
from .models import Order, Client
from .forms import ImageForm

def index(request):
    return render(request, "seminar2_app/index.html")

def get_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    last_week_orders = Order.objects.filter(client=client, order_date__gte=datetime.now() - timedelta(days=7))
    last_month_orders = Order.objects.filter(client=client, order_date__gte=datetime.now() - timedelta(days=30))
    last_year_orders = Order.objects.filter(client=client, order_date__gte=datetime.now() - timedelta(days=365))

    context = {
        'client': client,
        'last_week_orders': last_week_orders,
        'last_month_orders': last_month_orders,
        'last_year_orders': last_year_orders,
    }

    return render(request, "seminar2_app/orders.html", context)

def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, "seminar2_app/upload_image.html", {"form": form})