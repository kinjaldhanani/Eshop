# Generated by Django 4.0.4 on 2022-07-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0036_alter_order_total_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='points_gained',
            field=models.FloatField(default=0),
        ),
    ]
