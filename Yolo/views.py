from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .forms import RegisterForm,LoginForm 
from .models import Register

def home(request):
    return render(request,'Yolo/home.html')

def register(request):
    if request.method == 'POST':
        filled_form = RegisterForm(request.POST)
        if filled_form.is_valid():
            username = filled_form.cleaned_data['username']
            users = Register.objects.all()            
            flag=1
            for user in users:
                if user.username == username:
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

def login(request):
    if request.method == 'POST':
        filled_form = LoginForm(request.POST)
        if filled_form.is_valid():
            username = filled_form.cleaned_data['username']
            password = filled_form.cleaned_data['password']
            print(username)
            user = authenticate(username=username,password=password)
            if user is not None:
                if user.is_active():
                    login(request,user)
                    return redirect(request,'Yolo/home.html')
            else:
                form = LoginForm()
                note = "Wrong credentials"
                return render(request,'Yolo/login.html',{'note':note,'loginform':form})


    else:
        form = LoginForm()
        return render(request,'Yolo/login.html',{'loginform':form})   
