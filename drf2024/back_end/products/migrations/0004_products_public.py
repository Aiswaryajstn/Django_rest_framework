# Generated by Django 4.1 on 2024-03-19 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_products_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
