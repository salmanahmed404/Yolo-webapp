# Generated by Django 2.1.7 on 2019-04-12 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0002_auto_20190412_2118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotels',
            name='city',
        ),
        migrations.DeleteModel(
            name='hotels',
        ),
    ]