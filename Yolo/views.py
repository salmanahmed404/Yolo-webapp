from django.shortcuts import render
from .forms import RegisterForm 
from .models import Register

def home(request):
    return render(request,'Yolo/home.html')

def register(request):
    if request.method == 'POST':
        filled_form = RegisterForm(request.POST)
        if filled_form.is_valid():
            username = filled_form.cleaned_data['name']
            users = Register.objects.all()            
            flag=1
            for user in users:
                if user.name == username:
                    note='User already exists'
                    flag=0
                    break
            if flag == 1:
                filled_form.save
                note = 'Successful Registration'

            new_form = RegisterForm()
            return render(request,'Yolo/register.html',{'note':note,'registerform':new_form})

    else:
        new_form = RegisterForm()
        return render(request,'Yolo/register.html',{'registerform':new_form})        
