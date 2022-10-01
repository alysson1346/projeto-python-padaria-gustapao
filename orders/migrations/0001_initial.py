# Generated by Django 4.1 on 2022-10-01 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("withdrawal_date", models.DateTimeField()),
                ("comment", models.TextField()),
                ("is_finished", models.BooleanField(default=False, null=True)),
                (
                    "total",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("Pedido Confirmado", "Accepted"),
                            ("Pedido Recusado", "Denied"),
                            ("Seu pedido está sendo analisado", "Default"),
                        ],
                        default="Seu pedido está sendo analisado",
                        max_length=50,
                    ),
                ),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orders",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Order_Products",
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
                ("quantity", models.IntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="orders.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="order",
            name="products",
            field=models.ManyToManyField(
                related_name="orders",
                through="orders.Order_Products",
                to="products.product",
            ),
        ),
    ]
