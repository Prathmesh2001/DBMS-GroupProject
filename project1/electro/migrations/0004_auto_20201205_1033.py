# Generated by Django 3.1.3 on 2020-12-05 05:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electro', '0003_products_digital'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zipcode',
            new_name='pincode',
        ),
    ]
