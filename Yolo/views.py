from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.db import connection

def home(request):
    return render(request,'Yolo/home_new.html')

def sql_queries(request):
    print (connection.queries)
    return render(request,'Yolo/sql_queries.html')

