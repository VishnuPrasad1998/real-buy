# Generated by Django 3.1.2 on 2020-11-08 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0006_auto_20201108_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(blank=True, default='photos/2020/10/30/shwetha.jpg', upload_to='photos/%Y/%m/%d/'),
        ),
    ]