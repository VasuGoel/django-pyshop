from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    # return HttpResponse('Welcome to the products page!')
    return render(request, 'index.html', {'products': products})
