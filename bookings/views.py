from django.shortcuts import render
import json
from Yolo.models import City

def hotels(request):
    return render (request,'bookings/hotels.html') 
