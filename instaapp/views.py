from email.policy import HTTP
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import *
from instaapp.models import *
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    ingr_type = ['Recipe Base','Vegetables & Greens','Fruits & Berries', 'Meat','Baking','Dairy & Eggs','Herbs & Spices']
    ingr_name = Ingredients.objects.all()
    cat = catdetails.objects.all()
    rec = Recipe_info.objects.all()
    params = {'rec':rec,'cat':cat,'ingr_type':ingr_type,'ingr_name':ingr_name}
    return render(request, "index.html", params)

def login(request):
    return render(request, "account/login.html")


def contact(request):
    return render(request, "contact.html")

@login_required 
def requestrec(request):
    
    form = requestforms(request.POST)
    cat=catdetails.objects.all()
    context = {'cat':cat, 'form':form}

    if request.method == "POST":
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Recipe request has been submitted successfully.')
            return render(request, 'requestrecipe.html', context)
        else:
            messages.error(request, 'Invalid form submission')
            messages.error(request, form.errors)
    else:
        form = requestrecipe()
    return render(request, 'requestrecipe.html', context)

@login_required 
def details(request):
    ing = None
    list1=[]
    rec_name = request.GET.get("name")
    rec = Recipe_info.objects.filter(name = rec_name)
    for i in rec:
        rec_step = Recipe_step.objects.filter(name_id = i.id)
    for j in rec_step:
            ing = Ingredients.objects.filter(id = j.ingr_id)
            for k in ing:
                list1.append(k.ing_name)
                
    print(list1)
    form = feedbackforms(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/')
    else:
        form = feedbackforms()
    params = {'list1':list1,'rec':rec,'rec_step':rec_step,'ing':ing, 'form':form}

    return render(request,"detail.html",params)

# @login_required
# def addtocart_ingr(request):
#     ingr_type = ['Recipe Base','Vegetables & Greens','Fruits & Berries', 'Meat','Baking','Dairy & Eggs','Herbs & Spices']
#     ingr_name = Ingredients.objects.all()
    
#     if request.method == 'POST':
#         ingrs = request.POST.getlist('ingr_det')

#     list1 = []
#     for i in ingrs :
#         ing = Ingredients.objects.filter(ing_name = i)
#         print(ing)
#         list1.append(ing)
#     print(list1)
    
#     params = {'list1':list1,'ingr_type':ingr_type,'ingr_name':ingr_name}
#     return render(request,"cart.html",params)

@login_required
def cart(request):
    
    ingr_type = ['Recipe Base','Vegetables & Greens','Fruits & Berries', 'Meat','Baking','Dairy & Eggs','Herbs & Spices']
    ingr_name = Ingredients.objects.all()
    ingrs = request.POST.getlist('ingr_det')
    
    if request.method == 'POST':
        ingrs = request.POST.getlist('ingr_det')

    list1 = []
    for i in ingrs :
        ing = Ingredients.objects.filter(ing_name = i)
        # for pid, pname, ptotal, __ in zip(pdi, pdi, pdi, pdi):
        #     models.Sellinvoiceitems.objects.create(
        #         productid=pid
        #         productname=pname,
        #         totalnumber=ptotal,
        #         sellinvoice = invoice,
        #         stockid = stock
        #     )
        print(User.id)
        print(ing)
        list1.append(ing)
    print(list1)
    
    params = {'list1':list1,'ingr_type':ingr_type,'ingr_name':ingr_name}
    return render(request,"cart.html",params)


def search(request):
    query = request.GET['query']
    allPost = Recipe_info.objects.filter(name__icontains = query) 
    params = {'allPost':allPost}
    return render(request,"search_recipe.html",params)

def search_cat(request):
    cat_btn = request.GET['cat_btn']
    cat_id = catdetails.objects.get(cat_name=cat_btn)
    cat=Recipe_info.objects.filter(cat_name_id = cat_id.id)
    params = {'cat':cat}
    return render(request,"search_cat.html",params)

def search_ingr(request):
    chk = 0
    rec = None
    list1 = []
    if request.method == 'POST':
        ingrs = request.POST.getlist('ingrs')
    print(ingrs)
    
    for i in ingrs:
        in_id = Ingredients.objects.filter(ing_name=i)
        print(in_id)
        for j in in_id:
            all_step = Recipe_step.objects.filter(ingr_id = j.id)
            print(all_step)
            for k in all_step:
                if(len(ingrs) > 1):    
                    if(chk == k.name_id):
                        rec = Recipe_info.objects.filter(id = k.name_id)
                        list1.append(rec)
                    chk= k.name_id
                else:
                    rec = Recipe_info.objects.filter(id = k.name_id)
                    list1.append(rec)
                    print(rec)   

    params = {'list1':list1}
    print(list1)

    
    return render(request,"search_ingr.html",params)

def contact(request):
    return render(request,"contact.html")

# def userfb(request):
#     # form = feedbackforms(request.POST)
#     # context = {'form':form}        
#     # if form.is_valid():
#     #     form.save()
#     #     messages.success(request, 'Feedback has been submitted successfully.')
#     #     return render(request, 'detail.html', {'form':form})
#     # else:
#     #     messages.error(request, 'Invalid form submission')
#     #     messages.error(request, form.errors)
#     #     form = feedbackforms()
#     # return render(request, 'detail.html', {'form':form})

