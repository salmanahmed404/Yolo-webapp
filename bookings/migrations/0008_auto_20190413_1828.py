# Generated by Django 2.1.7 on 2019-04-13 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_auto_20190413_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='ac',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hotels',
            name='breakfast',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hotels',
            name='cctv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='hotels',
            name='wifi',
            field=models.BooleanField(default=False),
        ),
    ]
