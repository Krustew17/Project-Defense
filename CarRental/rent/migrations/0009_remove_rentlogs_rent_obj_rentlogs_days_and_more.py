# Generated by Django 4.2.1 on 2023-08-10 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rent', '0008_rentmodel_car_rented'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentlogs',
            name='rent_obj',
        ),
        migrations.AddField(
            model_name='rentlogs',
            name='days',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rentlogs',
            name='rented_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Rented_to_User', to=settings.AUTH_USER_MODEL),
        ),
    ]
