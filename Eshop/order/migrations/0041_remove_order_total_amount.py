# Generated by Django 4.0.4 on 2022-07-15 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0040_order_total_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
    ]