from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from instaapp.models import Recipe_detail

# Create your views here.
def index(request):
    rec=Recipe_detail.objects.all()
    return render(request, "index.html",{'rec':rec})

def login(request):
    return render(request, "login.html")

@login_required
def cart(request):
    return render(request, "cart.html")

def contact(request):
    return render(request, "contact.html")

@login_required 
def requestrecipe(request):
    return render(request, "Requestrecipe.html") 


