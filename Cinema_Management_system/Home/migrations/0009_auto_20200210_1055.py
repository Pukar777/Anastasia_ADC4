# Generated by Django 3.0.1 on 2020-02-10 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0008_auto_20200210_1054'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='movie',
            new_name='movies',
        ),
    ]
