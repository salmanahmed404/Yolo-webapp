from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta():
        model = Register
        fields = ['username','email','password']
        widgets = {
            'password': forms.PasswordInput()
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)