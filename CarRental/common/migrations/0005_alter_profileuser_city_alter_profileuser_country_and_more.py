# Generated by Django 4.2.1 on 2023-07-04 10:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_alter_profileuser_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileuser',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(inverse_match=True, message='City field can contain only characters.', regex='^[A-Za-z]+$')], verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(inverse_match=True, message='Country field can contain only characters.', regex='^[A-Za-z]+$')], verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(inverse_match=False, message='First Name field can contain only characters.', regex='^[A-Za-z]+$')], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(inverse_match=True, message='Last Name field can contain only characters.', regex='^[A-Za-z]+$')], verbose_name='Last Name'),
        ),
    ]
