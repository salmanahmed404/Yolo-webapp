from django.shortcuts import render, redirect
import json
import MySQLdb
from Yolo.models import City
from .models import Hotels
from .forms import Select_City,Book_Hotel
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


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
                hotel_pk = var.id
                return render(request, 'bookings/find_hotels_new.html', 
                {
                    'hotel': var,
                    'hotel_pk':hotel_pk
                    })

def book(request,pk):
    if request.method == 'POST':
        print('Requested post')
        hotel_obj = Hotels.objects.get(pk=pk)
        filled_hotelform = Book_Hotel(request.POST)
        
        if not filled_hotelform.is_valid():
            
            print('form validated')
            if filled_hotelform.cleaned_data['room_type'] == 'single_room':
                hotel_obj.single_room_number -= filled_hotelform.cleaned_data['number_of_rooms']
                hotel_obj.save()
                #filled_hotelform.save()
            elif filled_hotelform.cleaned_data['room_type'] == 'double_room':
                print("Entered")
                hotel_obj.double_room_number -= filled_hotelform.cleaned_data['number_of_rooms']
                hotel_obj.save()
                #filled_hotelform.save()
            elif filled_hotelform.cleaned_data['room_type'] == 'executive_room':
                hotel_obj.executive_room_number -= filled_hotelform.cleaned_data['number_of_rooms']
                hotel_obj.save()
                #filled_hotelform.save()
        else:
#            print(f'Room type : {room_type_}\nNumber of room : {number_rooms_}')
            return HttpResponseRedirect(request.path_info)  # redirects to same page if form validation failed
                
        return redirect('response')    

    else:
        hotel_form = Book_Hotel()
        hotel_obj = Hotels.objects.get(pk=pk)
        primary_key = hotel_obj.id
        return render(request,'bookings/book.html',{'hotel_form':hotel_form,'hotel_obj':hotel_obj,'pk':primary_key})    

def response(request):
    return render(request,'bookings/response_new.html')

def data(request):

    """json_data = open('static/city_mock_new2.json',encoding='utf8')
    data = json.load(json_data)
    for val in data:
        a = City(city_name=val['city_name'])
        a.save()
        print("Successful")"""

    json_data2 = open('static/hotels_mock_new2.json',encoding='utf8')
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
        i = i+1
    return render(request, 'bookings/data.html')
