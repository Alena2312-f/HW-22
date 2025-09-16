from django.urls import include, path

from catalog.apps import CatalogConfig
from catalog.views import contacts, home, product, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("", home, name="home"),
    path("contacts/", contacts, name="contacts"),
    path("product/", product, name="product"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
]
