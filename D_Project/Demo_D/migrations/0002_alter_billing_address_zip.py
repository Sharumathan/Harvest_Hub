# Generated by Django 5.0.3 on 2024-04-08 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Demo_D', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing_address',
            name='Zip',
            field=models.IntegerField(default=''),
        ),
    ]