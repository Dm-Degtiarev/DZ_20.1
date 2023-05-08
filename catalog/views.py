from django.shortcuts import render
from catalog.models import Product, Contacts



def index(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/index.html', context)


def contacts(request):
    contacts = Contacts.objects.all()

    context = {
        'all_contacts': contacts,
    }

    return render(request, 'catalog/contacts.html', context)


def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }

    return render(request, 'catalog/products.html', context)
