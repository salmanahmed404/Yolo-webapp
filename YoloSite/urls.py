from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Yolo import views as Yolo_views
from users import views as users_views
from bookings import views as bookings_views
from rail_booking import views as rail_views
from django.conf import settings
import debug_toolbar

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('',Yolo_views.home,name='home'),
    path('register/',users_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login_new.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='Yolo/home_new.html'),name='logout'), 
    path('hotels/',bookings_views.hotels,name='hotels'),
    path('data/',bookings_views.data,name='data'),
    path('find_hotels/',bookings_views.find_hotels,name='find_hotels'),
    path('book/<int:pk>',bookings_views.book,name='book'),
    path('response/',bookings_views.response,name='response'),
    path('sql_queries/',Yolo_views.sql_queries,name='sql_queries'),
    path('find_trains/',rail_views.find_trains,name='find_trains'),
    path('get_trains/',rail_views.get_trains,name='get_trains'),
]
