# Generated by Django 4.0.4 on 2022-06-23 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_category'),
        ('order', '0011_remove_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='product',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='product.product'),
        ),
    ]
