# Generated by Django 2.1.7 on 2019-04-15 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0014_remove_hotel_input_booking_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel_input',
            name='booking_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='hotel_input',
            name='number_of_adults',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3')], default=0),
        ),
        migrations.AlterField(
            model_name='hotel_input',
            name='number_of_children',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', '1'), ('2', '2')], default=0),
        ),
    ]