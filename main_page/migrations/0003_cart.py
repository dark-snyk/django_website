# Generated by Django 4.2 on 2023-04-29 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_rename_product_des_product_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_product_quantity', models.IntegerField()),
                ('total_for_product', models.FloatField()),
                ('user_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.product')),
            ],
        ),
    ]
