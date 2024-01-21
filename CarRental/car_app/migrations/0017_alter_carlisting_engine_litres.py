# Generated by Django 4.2.1 on 2023-08-11 21:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0016_alter_carlisting_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carlisting',
            name='engine_litres',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, message='You cannot have an engine below 0.0 litres.'), django.core.validators.MaxValueValidator(8, message='You cannot have an engine above 8 litres.')], verbose_name='Engine Litres'),
        ),
    ]
