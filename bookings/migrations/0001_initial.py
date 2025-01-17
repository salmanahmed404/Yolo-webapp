# Generated by Django 2.1.7 on 2019-04-12 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Yolo', '0006_auto_20190406_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
                ('rating', models.FloatField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yolo.City')),
            ],
        ),
    ]
