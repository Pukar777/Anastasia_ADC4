# Generated by Django 3.0.1 on 2020-01-10 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('Cinema_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('Cinema_address', models.CharField(blank=True, max_length=50)),
                ('Cinema_email', models.EmailField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Customer_name', models.CharField(max_length=30)),
                ('Customer_id', models.CharField(max_length=7, primary_key=True, serialize=False)),
                ('Customer_address', models.CharField(blank=True, max_length=50)),
                ('Customer_contactNo', models.IntegerField()),
            ],
        ),
    ]
