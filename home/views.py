from django.shortcuts import render
from products.models import Product
#from .models import Product  
# Create your views here.

def index(request):
    """ A view to return the index page """
    
    return render(request, 'home/index.html'),

def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'home/search_results.html', {'products': products})
