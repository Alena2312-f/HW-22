from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product

class HomeView(TemplateView):
    """Kонтроллер для отображения домашней страницы"""
    template_name = 'catalog/home.html'

class ContactsView(TemplateView):
    """Контроллер для отображения страницы с контактной информацией"""
    template_name = 'catalog/contacts.html'



class ProductListView(ListView):
    """Контроллер для отображения страницы с продукцией"""
    model = Product


class ProductDetailView(DetailView):
    """Контроллер для отображения страницы с отдельной продукцией"""
    model = Product

