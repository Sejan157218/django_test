from django.shortcuts import render  
from .models import Product

def index(request):  

   data = Product.objects.all()

   return render(request, 'index.html',{'data':data})