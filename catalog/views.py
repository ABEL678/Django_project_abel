from django.shortcuts import render

from catalog.models import Product


def index(request):
    content = {
        'object_list': Product.objects.all(),
            }
    return render(request, 'catalog/index.html', content)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def home(request):
    return render(request, 'catalog/home.html')
