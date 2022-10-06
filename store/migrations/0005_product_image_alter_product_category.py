# Generated by Django 4.1.1 on 2022-10-05 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_alter_product_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("all", "All"),
                    ("laptopaccessories", "Laptop & accessories"),
                    ("electronics", "electronics"),
                    ("apparel", "Apparel"),
                ],
                default="all",
                max_length=500,
                null=True,
            ),
        ),
    ]
