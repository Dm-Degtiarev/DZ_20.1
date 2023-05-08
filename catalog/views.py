from django.shortcuts import render
from catalog.models import Product, Contacts


def index(request):
    return render(request, 'catalog/index.html')


def catalog(request):
    latest_products = Product.objects.all()[:5]
    context = {
        'latest_products': latest_products,
    }
    for product in latest_products:
        print(product.product_name)

    return render(request, 'catalog/catalog.html', context)


def contacts(request):
    contacts = Contacts.objects.all()

    context = {
        'all_contacts': contacts,
    }

    return render(request, 'catalog/contacts.html', context)
