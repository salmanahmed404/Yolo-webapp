from django.shortcuts import render,redirect
import json,MySQLdb
from Yolo.models import City
from .models import Hotels
from .forms import Select_City
from django.contrib.auth.decorators import login_required

@login_required
def hotels(request):
<<<<<<< HEAD
    json_data = open('static/city_mock.json')
    data1 = json.load(json_data)
    data2 = json.dumps(data1)
    data3 = json.loads(data2)
    print(data3)
    return render (request,'bookings/hotels.html')
=======
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
    
    #print("Connected")
    return render (request,'bookings/data.html')    
>>>>>>> ed81aa0fe66d1fd3e4fafe7007f6874685ca1c39
