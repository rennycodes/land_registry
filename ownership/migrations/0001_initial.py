# Generated by Django 5.0.1 on 2024-02-08 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landowner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(default='Someone@tonek.com', max_length=254)),
                ('inputter_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LandProperty',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coordinates', models.DecimalField(decimal_places=6, max_digits=10, null=True)),
                ('land_type', models.CharField(max_length=255)),
                ('other_details', models.TextField(blank=True, null=True)),
                ('inputter_name', models.CharField(blank=True, max_length=255, null=True)),
                ('landowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ownership.landowner')),
            ],
        ),
    ]
