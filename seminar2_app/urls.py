from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="index"),
    path("orders/<int:client_id>/", views.get_orders, name="orders"),
    path('upload/', views.upload_image, name='upload_image'),
    path('products/', views.product_list, name='product_list'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:pk>/', views.edit_product, name='edit_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)