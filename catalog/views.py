from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product

class HomeView(TemplateView):
    """Kонтроллер для отображения домашней страницы"""
    template_name = 'catalog/home.html'

class ContactsView(TemplateView):
    """Контроллер для отображения страницы с контактной информацией"""
    template_name = 'catalog/contacts.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'page_obj'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.all().order_by('-created_at')[:5]
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
