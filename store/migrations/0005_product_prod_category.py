# Generated by Django 4.2.3 on 2023-08-05 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
