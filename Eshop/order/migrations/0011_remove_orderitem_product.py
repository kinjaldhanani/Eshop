# Generated by Django 4.0.4 on 2022-06-23 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0010_orderitem_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
    ]
