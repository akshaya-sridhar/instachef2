from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from instaapp.models import Recipe_detail, Recipe_info, catdetails

# Create your views here.
def index(request):
    rec=Recipe_info.objects.all()
    cat=catdetails.objects.all()
    params={'rec':rec, 'cat':cat}
    return render(request, "index.html",params)

def login(request):
    return render(request, "account/login.html")

@login_required
def cart(request):
    return render(request, "cart.html")

def contact(request):
    return render(request, "contact.html")

@login_required 
def requestrecipe(request):
    return render(request, "Requestrecipe.html") 


