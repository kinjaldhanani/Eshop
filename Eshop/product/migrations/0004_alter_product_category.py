# Generated by Django 4.0.4 on 2022-06-17 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_alter_category_parent'),
        ('product', '0003_rename_discription_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='category.category'),
        ),
    ]
