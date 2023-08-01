# Generated by Django 4.2.1 on 2023-08-01 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_alter_contactusmodel_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='email_token',
            field=models.CharField(default='12', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
