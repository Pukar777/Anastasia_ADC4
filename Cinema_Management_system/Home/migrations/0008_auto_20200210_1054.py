# Generated by Django 3.0.1 on 2020-02-10 05:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_auto_20200210_1053'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='Movie_title',
            new_name='movie',
        ),
    ]
