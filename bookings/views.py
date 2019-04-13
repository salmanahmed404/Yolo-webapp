from django.shortcuts import render
import json

def hotels(request):
    json_data = open('static/city_mock.json')
    data1 = json.load(json_data)
    data2 = json.dumps(data1)
    data3 = json.loads(data2)
    print(data3)
    return render (request,'bookings/hotels.html')
