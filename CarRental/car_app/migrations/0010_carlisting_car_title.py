# Generated by Django 4.2.1 on 2023-07-20 09:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0009_remove_carlisting_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlisting',
            name='car_title',
            field=models.CharField(default='test', max_length=50, validators=[django.core.validators.MinLengthValidator(5, message='Your car title should be at least 5 characters long.')]),
            preserve_default=False,
        ),
    ]
