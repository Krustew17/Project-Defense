# Generated by Django 4.2.1 on 2023-07-11 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0002_fill_data_into_car_make_and_car_model'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carmake',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='carmake',
            name='make',
            field=models.CharField(choices=[], max_length=16, unique=True, verbose_name='Make'),
        ),
    ]
