# Generated by Django 2.2.7 on 2019-11-21 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20191114_0411'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job1',
            old_name='image',
            new_name='image1',
        ),
        migrations.RenameField(
            model_name='job1',
            old_name='summary',
            new_name='summary1',
        ),
    ]
