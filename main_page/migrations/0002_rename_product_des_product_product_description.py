# Generated by Django 4.2 on 2023-04-28 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_des',
            new_name='product_description',
        ),
    ]
