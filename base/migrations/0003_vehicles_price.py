# Generated by Django 4.2.4 on 2023-09-26 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_vehicles_image_orders_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicles',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
