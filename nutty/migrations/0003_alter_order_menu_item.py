# Generated by Django 4.2.10 on 2024-02-25 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutty', '0002_order_menu_item_order_quantity_alter_order_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='menu_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nutty.menu'),
        ),
    ]
