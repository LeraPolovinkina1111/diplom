from django.core.paginator import Paginator
from django.shortcuts import get_list_or_404, get_object_or_404, render


def catalog(request):
    contex: dict[str, any] = {
        'title': 'Home - Каталог',
        'goods': [
            {'image': 'deps/images/goods/set of tea table and three chairs.jpg',
             'name': 'Хлеб',
             'description': 'Обычный хлеб',
             'price': 50.00},

            {'image': 'deps/images/goods/set of tea table and two chairs.jpg',
             'name': 'Молоко',
             'description': 'Молоко Талицкое',
             'price': 93.00},

            {'image': 'deps/images/goods/double bed.jpg',
             'name': 'Сметана',
             'description': 'Сметана Шадринская',
             'price': 67.00},

            {'image': 'deps/images/goods/kitchen table.jpg',
             'name': 'Мука',
             'description': 'Мука твердого помола',
             'price': 120.00},



        ]
    }

    return render(request, "goods/catalog.html", contex)


def product(request, product_slug):
    return render(request, "goods/product.html")
