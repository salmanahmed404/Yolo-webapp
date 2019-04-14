from django.shortcuts import render, redirect
import json
import MySQLdb
from Yolo.models import City
from .models import Hotels
from .forms import Select_City
from django.contrib.auth.decorators import login_required


@login_required
def hotels(request):
    city_form = Select_City()
    return render(request, 'bookings/hotels.html', {'city_form': city_form})


def find_hotels(request):
    filled_form = Select_City(request.POST)
    if filled_form.is_valid():
        obj = Hotels.objects.all()
        for var in obj:
            if filled_form.cleaned_data['city_name'] == var.city_name:
                return render(request, 'bookings/find_hotels_new.html', 
                {
                    'hotel': var,
                    })


def data(request):

    """json_data = open('static/city_mock_new2.json',encoding='utf8')
    data = json.load(json_data)
    for val in data:
        a = City(city_name=val['city_name'])
        a.save()
        print("Successful")"""

    """json_data2 = open('static/hotels_mock_new2.json',encoding='utf8')
    obj = City.objects.all()
    i = 0
    data2 = json.load(json_data2)
    for val in data2:
        a = Hotels(hotel_name=val['hotel_name'],
                   single_room_number=val['single_room_number'],
                   double_room_number=val['double_room_number'],
                   executive_room_number=val['executive_room_number'],
                   single_room_cost=val['single_room_cost'],
                   double_room_cost=val['double_room_cost'],
                   executive_room_cost=val['executive_room_cost'],
                   wifi=val['wifi'],
                   ac=val['ac'],
                   breakfast=val['breakfast'],
                   cctv=val['cctv'],
                   rating=val['rating'],
                   address=val['address'],
                   city_name=obj[i], )
        
        a.save()
        i = i+1"""
    return render(request, 'bookings/data.html')
