from django.shortcuts import render,redirect
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
            messages('invalid credentials')
    return render(request,'register.html',{'form':form})

def view_products(request):
    p=product.objects.all()
    return render(request,'products.html',{'p':p})

def search_btn(request):
    if request.method=="POST":
        search=request.POST['search'].lower()
        if (product.objects.filter(prod_category=search) or product.objects.filter(prod_subcategory=search) or product.objects.filter(prod_name=search)).exists():
            type=product.objects.filter(prod_category=search)
            brand=product.objects.filter(prod_subcategory=search)
            return render(request,'products.html',{'brand':brand,'type':type})
        else:
            print('not found')
    return render(request,'products.html')
