# Generated by Django 4.2.7 on 2023-11-29 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0017_delete_desserts_delete_dinner_delete_drinks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='stories',
            name='image6',
        ),
    ]
