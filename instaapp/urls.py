from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login, name='login'),
    path('cart', views.cart, name='cart'),
    path('contact', views.contact, name='contact'),
    path('requestrecipe', views.requestrecipe, name='requestrecipe'),
]