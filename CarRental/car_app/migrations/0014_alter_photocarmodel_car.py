# Generated by Django 4.2.1 on 2023-07-25 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0013_alter_photocarmodel_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photocarmodel',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='car_pics', to='car_app.carlisting'),
        ),
    ]