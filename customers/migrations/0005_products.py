# Generated by Django 5.0.1 on 2024-04-20 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_rename_views_graphdetails_customercount_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('product_title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('date_added', models.DateField()),
                ('life_time', models.IntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='productPhotos')),
            ],
        ),
    ]