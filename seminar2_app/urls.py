from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("orders/<int:client_id>/", views.get_orders, name="orders"),
    path('upload/', views.upload_image, name='upload_image'),
]