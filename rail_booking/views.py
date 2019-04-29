from django.shortcuts import render
from .forms import Trains
from .api_handler import getStation,getTrains

def find_trains(request):
    if request.method == 'POST':
        filled_form = Trains(request.POST)
        if filled_form.is_valid():
            src_stations = getStation(filled_form.cleaned_data['source'])
            dest_stations = getStation(filled_form.cleaned_data['dest'])
            button_text = 'Find Trains'
            find_train_form = Trains()
            station_select = False
            return render(request,'rail_booking/find_trains.html',{'form':find_train_form,'src_stations':src_stations,'dest_stations':dest_stations,'button_text':button_text,'station_select':station_select})
    else:
        find_train_form = Trains()
        station_select = True
        button_text = 'Find city stations'
        return render(request,'rail_booking/find_trains.html',{'form':find_train_form,'button_text':button_text,'station_select':station_select})

def get_trains(request):
    if request.method == 'POST':
        filled_form = Trains(request.POST)
        if filled_form.is_valid():
            print("Entered")
            trains = getTrains(filled_form.cleaned_data['source'],filled_form.cleaned_data['dest'],'24/06/2017')
            return render(request,'rail_booking/get_trains.html',{'trains':trains})