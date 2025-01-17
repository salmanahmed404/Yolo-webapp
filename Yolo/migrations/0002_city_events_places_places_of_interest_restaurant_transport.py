# Generated by Django 2.1.7 on 2019-03-25 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Yolo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('place_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yolo.City')),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=50)),
                ('lat', models.FloatField(max_length=10)),
                ('lon', models.FloatField(max_length=10)),
                ('description', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('city_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yolo.City')),
            ],
        ),
        migrations.CreateModel(
            name='Places_Of_Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotspot', models.CharField(max_length=100)),
                ('place_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yolo.City')),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('rating', models.IntegerField()),
                ('contact_no', models.CharField(max_length=100)),
                ('place_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yolo.City')),
            ],
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_transport', models.CharField(max_length=100)),
                ('means_of_transport', models.CharField(max_length=200)),
                ('place_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Yolo.City')),
            ],
        ),
    ]
