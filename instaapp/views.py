from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

def cart(request):
    return render(request, "cart.html")

def contact(request):
    return render(request, "contact.html")

def requestrecipe(request):
    return render(request, "requestrecipe.html") 


