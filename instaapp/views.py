from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, "login.html")

@login_required
def cart(request):
    return render(request, "cart.html")

def contact(request):
    return render(request, "contact.html")

@login_required 
def requestrecipe(request):
    return render(request, "requestrecipe.html") 


