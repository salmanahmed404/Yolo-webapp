from django import forms
from .models import Hotels,Hotel_Input

class Select_City(forms.ModelForm):
    class Meta:
        model = Hotels
        fields = ['city_name']
        labels : {
            'city_name':'City Name',
        }

class Book_Hotel(forms.ModelForm):
    class Meta:
        model = Hotel_Input
        fields = ['name','room_type','number_of_rooms','number_of_adults','number_of_children','contact']
        labels : {
            'name':'Name',
            'room_type' : 'Room Type',
            'number_of_rooms' : 'Number of Rooms',
            'number_of_adults' : 'Number of Adults',
            'number_of_children' : 'Number of Children',
            'contact' : 'Contact Number'
        }