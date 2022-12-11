from django.shortcuts import render
from multiprocessing import context
from .models import product

# Create your views here.
def Page(request):
    first = product.objects.all()
    context = {
        'product': first  
    }
    return render(request, 'figourlist/product.html', context)