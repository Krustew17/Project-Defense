# Generated by Django 4.2.1 on 2023-08-09 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0016_alter_carlisting_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rent', '0003_alter_rentmodel_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentmodel',
            name='car_rented',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='car_app.carlisting'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rentmodel',
            name='rented_from',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='Rented_from_User', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
