# Generated by Django 4.0.4 on 2022-07-08 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0025_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
    ]
