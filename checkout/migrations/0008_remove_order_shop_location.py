# Generated by Django 3.1.3 on 2020-12-18 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_remove_orderlineitem_shop_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shop_location',
        ),
    ]
