from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import *
from . forms import *

# Create your views here.

def index(request):
    return render(request,'index.html')

def register(request):
    form=UserCreation()
    if request.method=="POST":
        form=UserCreation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            messages.error(request,'invalid credentials')
    return render(request,'register.html',{'form':form})

@login_required
def view_products(request):
    p=product.objects.all()
    return render(request,'products.html',{'p':p})

@login_required
def search_btn(request):
    if request.method=="POST":
        search=request.POST['search'].lower()
        if search=='':
            return redirect('/')
        elif (product.objects.filter(prod_category=search) or product.objects.filter(prod_subcategory=search) or product.objects.filter(prod_name=search)).exists():
            type=product.objects.filter(prod_category=search)
            brand=product.objects.filter(prod_subcategory=search)
            return render(request,'products.html',{'brand':brand,'type':type})
        else:
            messages.error(request,"Sorry,couldn't find..")
    return render(request,'products.html')

def filter_catg(request,filter):
    if product.objects.filter(prod_subcategory=filter).exists():
        brand=product.objects.filter(prod_subcategory=filter)
        return render(request,'products.html',{'brand':brand,'type':type})
    return render(request,'products.html')
