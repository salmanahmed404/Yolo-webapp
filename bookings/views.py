from django.shortcuts import render,redirect
import json
from Yolo.models import City
from .models import Hotels
from .forms import Select_City

def hotels(request):
    city_form = Select_City()
    return render (request,'bookings/hotels.html',{'city_form':city_form})

def find_hotels(request):
    return render (request,'bookings/find_hotels.html')


def data(request):
    
    print('Cities and hotels already entered ')
    return render (request,'bookings/data.html')    
