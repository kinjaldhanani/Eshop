# Generated by Django 4.0.4 on 2022-06-16 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_cart_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
    ]
