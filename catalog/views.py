from django.shortcuts import render


def index(request):
    return render(request, 'catalog/index.html')


def catalog(request):
    return render(request, 'catalog/catalog.html')
