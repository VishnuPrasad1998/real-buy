# Generated by Django 3.1.2 on 2020-11-17 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortlist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortlist',
            name='message',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]