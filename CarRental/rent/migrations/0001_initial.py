# Generated by Django 4.2.1 on 2023-08-01 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=60)),
                ('days', models.PositiveIntegerField()),
                ('rent_status', models.CharField(choices=[('Pending', 'Pending'), ('Rented', 'Rented'), ('Cancelled', 'Cancelled')], default='Pending', max_length=9)),
                ('rent_date', models.DateTimeField(auto_now_add=True)),
                ('rented_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Rented_to_User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
