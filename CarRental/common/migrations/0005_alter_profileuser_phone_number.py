# Generated by Django 4.2.1 on 2023-06-28 11:42

import CarRental.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_profileuser_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='phone_number',
            field=models.IntegerField(validators=[CarRental.common.validators.validate_phone_number_length], verbose_name='Phone Number'),
        ),
    ]
