# Generated by Django 4.0.10 on 2024-02-16 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='text',
            new_name='title',
        ),
    ]
