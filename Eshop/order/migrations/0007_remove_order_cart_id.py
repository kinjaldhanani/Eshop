# Generated by Django 4.0.4 on 2022-06-23 07:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_remove_order_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cart_id',
        ),
    ]
