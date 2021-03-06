# Generated by Django 3.1.2 on 2020-11-17 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shortlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=200)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('user_id', models.IntegerField(blank=True)),
                ('shortlist_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('slot', models.CharField(choices=[('FN', 'FORENOON'), ('AN', 'AFTERNOON')], max_length=50)),
            ],
        ),
    ]
