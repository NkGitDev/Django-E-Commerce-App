# Generated by Django 4.2.3 on 2023-08-05 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_prod_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]