# Generated by Django 4.2.3 on 2023-08-05 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='prod_decs',
            new_name='prod_desc',
        ),
    ]
