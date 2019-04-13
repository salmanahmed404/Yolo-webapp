from django.shortcuts import render,redirect
import json,MySQLdb
from Yolo.models import City
from .models import Hotels
from .forms import Select_City
from django.contrib.auth.decorators import login_required

@login_required
def hotels(request):
    city_form = Select_City()
    return render(request,'bookings/hotels.html',{'city_form':city_form})


def find_hotels(request):
    filled_form = Select_City(request.POST)
    if filled_form.is_valid():
        obj = Hotels.objects.all()
        for var in obj:
            if filled_form.cleaned_data['city_name'] == var.city_name:
                name = var.hotel_name
                return render (request,'bookings/find_hotels.html',{'name':name})    


def data(request):
    
    """json_data = open('static/city_mock.json')
    data = json.load(json_data)
    for val in data:
        a = City(city_name=val['city_name'])
        a.save()
        print("Successful")"""
    
    """json_data = open('static/hotels_mock.json')
    obj = City.objects.all()
    i = 0
    data = json.load(json_data)
    for val in data:
        a = Hotels(hotel_name=val['hotel_name'],rating=val['rating'],city_name=obj[i])
        i = i+1
        a.save()"""
    return render (request,'bookings/data.html')    
