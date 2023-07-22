# Generated by Django 4.2.1 on 2023-07-04 09:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_contactusmodel_alter_profileuser_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactusmodel',
            name='name',
            field=models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(inverse_match=False, message='Name field can contain only characters.', regex='[a-zA-Z]+')], verbose_name='Name'),
        ),
    ]