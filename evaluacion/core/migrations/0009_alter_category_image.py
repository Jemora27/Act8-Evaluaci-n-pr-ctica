# Generated by Django 4.1 on 2022-08-22 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='media/', verbose_name='Imagen de la categoria'),
        ),
    ]
