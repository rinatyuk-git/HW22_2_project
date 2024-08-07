# Generated by Django 5.0.6 on 2024-07-09 12:40

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(
                        help_text="Введите название категории",
                        max_length=100,
                        verbose_name="Название категории",
                    ),
                ),
                (
                    "category_info",
                    models.TextField(
                        help_text="Введите информацию о категории",
                        max_length=1255,
                        verbose_name="Информация о категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(
                        help_text="Введите название продукта",
                        max_length=100,
                        verbose_name="Название продукта",
                    ),
                ),
                (
                    "product_info",
                    models.TextField(
                        help_text="Введите информацию о продукте",
                        max_length=1255,
                        verbose_name="Информация о продукте",
                    ),
                ),
                (
                    "product_image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение продукта",
                        null=True,
                        upload_to="product/images",
                        verbose_name="Изображение продукта",
                    ),
                ),
                (
                    "product_price",
                    models.DecimalField(
                        decimal_places=2,
                        help_text="Задайте цену продукта",
                        max_digits=10,
                        verbose_name="Цена продукта",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        auto_now_add=True,
                        help_text="Задайте дату внесения продукта",
                        verbose_name="Дата внесения продукта",
                    ),
                ),
                (
                    "updated_at",
                    models.DateField(
                        auto_now=True,
                        help_text="Задайте дату последнего изменения продукта",
                        verbose_name="Дата последнего изменения продукта",
                    ),
                ),
                (
                    "manufactured_at",
                    models.DateField(
                        default=datetime.date(2024, 7, 9),
                        help_text="Задайте дату производства продукта",
                        verbose_name="Дата производства продукта",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Выберите категорию продукта",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ["product_name", "category"],
            },
        ),
    ]
