from django.db import models
from Yolo.models import City
#from phone_field import PhoneField

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

    address = models.CharField(max_length=200,default="some address")


    city_name = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_name 

class Hotel_Input(models.Model):
    name = models.CharField(max_length=30,blank=True)
    ADULTS_CHOICES = (
        (0,'0'),
        (1,'1'),
        (2,'2'),
        (3,'3'),
    )
    number_of_adults = models.PositiveSmallIntegerField(choices=ADULTS_CHOICES,blank=True,default=0)
    number_of_children = models.PositiveSmallIntegerField(choices=ADULTS_CHOICES,blank=True,default=0)
    contact = models.CharField(max_length=12,blank=True)

    booking_id = models.IntegerField(default=0)
    ROOM_TYPES = (
        ('single_room','Single Room'),
        ('double_room','Double Room'),
        ('executive_room','Executive Room')
    )
    room_type = models.CharField(max_length=50,choices=ROOM_TYPES ,blank=True)

    number_of_rooms = models.IntegerField()
