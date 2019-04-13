from django.db import models
from Yolo.models import City

class Hotels(models.Model):
    hotel_name = models.CharField(max_length=50)
    rating = models.FloatField()    

    single_room_number = models.IntegerField(default=0)
    double_room_number = models.IntegerField(default=0)
    executive_room_number = models.IntegerField(default=0)

    single_room_cost = models.FloatField(default=0)
    double_room_cost = models.FloatField(default=0)
    executive_room_cost = models.FloatField(default=0)

    wifi = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)


    city_name = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_name 

class Hotel_Input(models.Model):
    room_type = models.CharField(max_length=50,choices=[('single_room','Single Room'),('double_room','Double Room'),('executive_room','Executive Room')],blank=True)

    number_of_rooms = models.IntegerField()
