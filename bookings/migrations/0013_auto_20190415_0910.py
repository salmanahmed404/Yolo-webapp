# Generated by Django 2.1.7 on 2019-04-15 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0012_auto_20190415_0909'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel_input',
            old_name='booking_number',
            new_name='booking_id',
        ),
    ]
