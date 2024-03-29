# Generated by Django 4.2.1 on 2023-08-08 21:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_alter_profileuser_revenue_last_month_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserRevenue',
            fields=[
                ('revenue_today', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('revenue_yesterday', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('revenue_last_week', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('revenue_last_month', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('total_revenue', models.DecimalField(decimal_places=0, default=0, max_digits=10)),
                ('revenue_last_updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='revenue', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='revenue_last_month',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='revenue_last_updated',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='revenue_last_week',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='revenue_today',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='revenue_yesterday',
        ),
        migrations.RemoveField(
            model_name='profileuser',
            name='total_revenue',
        ),
    ]
