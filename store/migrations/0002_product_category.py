# Generated by Django 4.1.1 on 2022-10-05 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("all", "All"),
                    ("laptopaccessories", "Laptop & accessories"),
                    ("electronics", "electronics"),
                ],
                max_length=500,
                null=True,
            ),
        ),
    ]
