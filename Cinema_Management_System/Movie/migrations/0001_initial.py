# Generated by Django 3.0.1 on 2020-01-25 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('Movie_title', models.CharField(max_length=30)),
                ('Movie_License', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Movie_genre', models.CharField(max_length=30)),
                ('Movie_releaseDate', models.DateField(editable=False)),
                ('Movie_finalShowDate', models.DateField()),
            ],
        ),
    ]
