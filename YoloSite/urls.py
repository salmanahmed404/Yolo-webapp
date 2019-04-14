"""YoloSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from Yolo import views as Yolo_views
from users import views as users_views
from bookings import views as bookings_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Yolo_views.home,name='home'),
    path('register',users_views.register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='users/login_new.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='Yolo/home_new.html'),name='logout'), 
    path('hotels',bookings_views.hotels,name='hotels'),
    path('data',bookings_views.data,name='data'),
<<<<<<< HEAD
    path('find_hotels',bookings_views.find_hotels,name='find_hotels'),  
    path('bookings',bookings_views.bookings,name="bookings"),   
=======
    path('find_hotels',bookings_views.find_hotels,name='find_hotels'),
    path('book/<int:pk>',bookings_views.book,name='book'),
    path('response',bookings_views.response,name='response'),
>>>>>>> 4842c0d7be32ec50fb75dbdb20b7f610c92979db
]
