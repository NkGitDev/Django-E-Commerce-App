# Generated by Django 4.2.3 on 2023-08-09 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_rename_order_addr_orders_order_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='order_status',
            field=models.BooleanField(default=False),
        ),
    ]
