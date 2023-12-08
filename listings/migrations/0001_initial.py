# Generated by Django 5.0 on 2023-12-08 04:56

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('bedrooms', models.CharField(max_length=200)),
                ('bathrooms', models.CharField(max_length=200)),
                ('garage', models.CharField(max_length=200)),
                ('sqft', models.CharField(max_length=200)),
                ('lot_size', models.CharField(max_length=200)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%M/%d')),
                ('photo_1', models.ImageField(upload_to='photos/%Y/%M/%d')),
                ('photo_2', models.ImageField(upload_to='photos/%Y/%M/%d')),
                ('photo_3', models.ImageField(upload_to='photos/%Y/%M/%d')),
                ('photo_4', models.ImageField(upload_to='photos/%Y/%M/%d')),
                ('photo_5', models.ImageField(upload_to='photos/%Y/%M/%d')),
                ('photo_6', models.ImageField(upload_to='photos/%Y/%M/%d')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]
