from django.shortcuts import render
import json
from Yolo.models import City

def hotels(request):
    json_data = open('static/city_mock.json')
    print(type(json_data))
    data = json.load(json_data)
    print(type(data))
    for val in data:
        name = City(city_name=val['city_name'])
        name.save()
    return render (request,'bookings/hotels.html')
