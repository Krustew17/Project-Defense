# Generated by Django 4.2.1 on 2023-07-04 09:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(inverse_match=True, message='Name field can contain only characters.', regex='[a-zA-Z]+')], verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('topic', models.CharField(max_length=35, verbose_name='Topic')),
                ('message', models.TextField(max_length=300, verbose_name='Message')),
            ],
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='city',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.RegexValidator(inverse_match=True, message='City field can contain only characters.', regex='[a-zA-Z]+')], verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='country',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(inverse_match=True, message='Country field can contain only characters.', regex='[a-zA-Z]+')], verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(inverse_match=True, message='First Name field can contain only characters.', regex='[a-zA-Z]+')], verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='profileuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, validators=[django.core.validators.MinLengthValidator(3), django.core.validators.RegexValidator(inverse_match=True, message='Last Name field can contain only characters.', regex='[a-zA-Z]+')], verbose_name='Last Name'),
        ),
    ]
