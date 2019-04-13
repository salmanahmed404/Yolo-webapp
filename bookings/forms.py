from django import forms
from .models import Hotels,Hotel_Input

class Select_City(forms.ModelForm):
    class Meta:
        model = Hotels
        fields = ['city_name']
        labels : {
            'city_name':'City',
        }

class Book_Hotel(forms.ModelForm):
    class Meta:
        model = Hotel_Input
        fields = ['room_type','number_of_rooms']