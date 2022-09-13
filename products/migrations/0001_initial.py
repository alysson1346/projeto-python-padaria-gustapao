# Generated by Django 4.1 on 2022-09-13 01:37

from django.db import migrations, models
import django.db.models.deletion
import products.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                (
                    "image_file",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="",
                        validators=[products.models.validate_file_size],
                    ),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("is_available", models.BooleanField(default=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to="products.category",
                    ),
                ),
                (
                    "ingredients",
                    models.ManyToManyField(
                        related_name="products", to="products.ingredient"
                    ),
                ),
            ],
        ),
    ]
