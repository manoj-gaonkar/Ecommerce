# Generated by Django 4.1.1 on 2022-10-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0009_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                blank=True,
                choices=[
                    ("all", "All"),
                    ("laptopaccessories", "Laptop & accessories"),
                    ("electronics", "electronics"),
                    ("apparel", "Apparel"),
                    ("smartphones", "Smartphones"),
                ],
                default="all",
                max_length=200,
                null=True,
            ),
        ),
        migrations.DeleteModel(
            name="Category",
        ),
    ]
