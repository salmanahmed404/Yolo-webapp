from django import forms

class Trains(forms.Form):
    source = forms.CharField(max_length=50,label='Source')
    dest = forms.CharField(max_length=50,label='Destination')
