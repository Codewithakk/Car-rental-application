# Generated by Django 4.2.4 on 2023-10-01 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_location_order_remove_customer_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='endRent',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='startRent',
            field=models.TextField(null=True),
        ),
    ]