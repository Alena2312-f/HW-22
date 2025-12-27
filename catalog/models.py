from django.db import models


# Create your models here.


class Category(models.Model):
    """Базовые настройки модели Category"""

    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True
    )  # Разрешаем пустое описание

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]  # Сортировка по умолчанию

    def __str__(self):
        return self.name


class Product(models.Model):
    """Базовые настройки модели Product"""

    name = models.CharField(max_length=255, verbose_name="Наименование")
    description = models.TextField(
        verbose_name="Описание", blank=True, null=True
    )  # Разрешаем пустое описание
    image = models.ImageField(
        upload_to="products/photo", verbose_name="Изображение", blank=True, null=True
    )  # Каталог для загрузки изображений
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )  # Связь с моделью Category
    purchase_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена за покупку"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]  # Сортировка по умолчанию

    def __str__(self):
        return self.name
