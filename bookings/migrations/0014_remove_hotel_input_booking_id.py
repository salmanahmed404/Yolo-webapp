# Generated by Django 2.1.7 on 2019-04-15 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0013_auto_20190415_0910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel_input',
            name='booking_id',
        ),
    ]