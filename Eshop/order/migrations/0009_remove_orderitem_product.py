# Generated by Django 4.0.4 on 2022-06-23 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_remove_order_quantity_alter_order_customer_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
    ]
