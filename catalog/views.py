from django.shortcuts import render


def home(request):
    """Kонтроллер для отображения домашней страницы"""

    return render(request, "home.html")


def contacts(request):
    """Контроллер для отображения страницы с контактной информацией"""

    return render(request, "contacts.html")
