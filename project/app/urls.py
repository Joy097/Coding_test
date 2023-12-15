from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
    path('page/', views.show_page),
    path('product/<int:pk>', views.product_list, name='product')
    ]
