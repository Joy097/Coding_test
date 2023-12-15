from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_page),
    path('product/<int:pk>', views.product_list, name='product')
    ]
