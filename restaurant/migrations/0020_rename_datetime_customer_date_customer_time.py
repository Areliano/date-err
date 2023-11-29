# Generated by Django 4.2.7 on 2023-11-29 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0019_remove_customer_time_alter_customer_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='datetime',
            new_name='date',
        ),
        migrations.AddField(
            model_name='customer',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]