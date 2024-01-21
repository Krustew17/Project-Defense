# Generated by Django 4.2.1 on 2023-07-11 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0003_alter_carmake_unique_together_alter_carmake_make'),
    ]

    operations = [
        migrations.AddField(
            model_name='carlisting',
            name='engine_litres',
            field=models.PositiveIntegerField(default=1, verbose_name='Engine Litres'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='carlisting',
            name='body_style',
            field=models.CharField(choices=[('Sedan', 'Sedan'), ('Coupe', 'Coupe'), ('SUV', 'SUV'), ('Hatchback', 'Hatchback'), ('Sports', 'Sports Car'), ('Wagon', 'Wagon')], max_length=10, verbose_name='Body Style'),
        ),
        migrations.AlterField(
            model_name='carlisting',
            name='drive_type',
            field=models.CharField(choices=[('FWD', 'FWD'), ('RWD', 'RWD'), ('AWD', 'AWD')], max_length=3, verbose_name='Drive Type'),
        ),
        migrations.AlterField(
            model_name='carlisting',
            name='engine_type',
            field=models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric')], max_length=8, verbose_name='Engine Type'),
        ),
        migrations.AlterField(
            model_name='carlisting',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='carlisting',
            name='transmission',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=9, verbose_name='Transmission'),
        ),
    ]
