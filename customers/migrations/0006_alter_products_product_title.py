# Generated by Django 5.0.1 on 2024-04-20 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
