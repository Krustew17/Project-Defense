# Generated by Django 4.2.1 on 2023-08-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0017_profileuser_revenue_last_month_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profileuser',
            name='total_revenue',
            field=models.IntegerField(default=0),
        ),
    ]
