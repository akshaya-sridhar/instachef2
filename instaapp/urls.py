from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login, name='login'),
    path('cart', views.cart, name='cart'),
    path('contact', views.contact, name='contact'),
    path('requestrecipe', views.requestrec, name='requestrecipe'),
    path('search',views.search, name='search'),
    path('details',views.details,name = 'details'),
    path('search_cat',views.search_cat,name='search_cat'),
    path('search_ingr',views.search_ingr,name='search_ingr'),
]