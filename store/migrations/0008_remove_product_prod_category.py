# Generated by Django 4.2.3 on 2023-08-05 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_prod_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='prod_category',
        ),
    ]
