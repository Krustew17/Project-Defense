# Generated by Django 4.2.1 on 2023-08-10 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0016_alter_carlisting_price'),
        ('rent', '0009_remove_rentlogs_rent_obj_rentlogs_days_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentlogs',
            name='Car_Rented',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='car_app.carlisting'),
        ),
    ]
