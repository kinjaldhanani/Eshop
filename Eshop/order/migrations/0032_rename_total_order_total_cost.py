# Generated by Django 4.0.4 on 2022-07-15 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0031_alter_order_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='total_cost',
        ),
    ]