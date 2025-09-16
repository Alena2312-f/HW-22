from django.shortcuts import render, get_object_or_404

from catalog.models import Product


def home(request):
    """Kонтроллер для отображения домашней страницы"""

    return render(request, "home.html")


def contacts(request):
    """Контроллер для отображения страницы с контактной информацией"""

    return render(request, "contacts.html")

def product(request):
    """Контроллер для отображения страницы с товарами"""
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product.html", context)


def product_detail(request, pk):
    """Контроллер для отображения страницы с товарами"""
    product = get_object_or_404(Product, pk=pk)
    context = {"product": product}
    return render(request, "product_detail.html", context)