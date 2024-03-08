from django.shortcuts import render


# Create your views here.

def catalog(request):
    return render(request, 'product/catalog.html')


def goods(request):
    return render(request, 'product/goods.html')
