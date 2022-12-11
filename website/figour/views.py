from multiprocessing import context
from django.shortcuts import render
from .models import fpfigours, about, fpporforoosh
# Create your views here.

def first_page(request):
    fpfigour_list = fpfigours.objects.all()
    porforoosh = fpporforoosh.objects.all()
    context = {
        'fpfigours': fpfigour_list,
        'por' : porforoosh,
    }
    return render(request, 'figour/list.html', context)


def details(request, id):
    figour = fpfigours.objects.get(id=id)
    context = {
        'fig': figour
    }
    return render(request, 'figour/detail.html', context)

def about(request):
    text = about
    context = {
        'text': text
    }
    return render (request, 'figour/about.html', context)

# def product(request):
#     return render(request, 'figour/product.html')
