from django.urls import path,include
from . import views 
from .views import ip_status

from django.contrib.auth import views as auth_views

 
 

urlpatterns = [
    path('',views.Loginpage,name='loginpage'),
    # path('',views.registerpage,name='registerpage'),
    path('register/',views.userregister,name='register'),
    
    path('loginuser/',views.loginuser,name='loginuser'),
    path('check/', views.check_arduino_status, name='checkstatus'),
    path('data/',views.store_arduino_data,name='arduinodata'),
     path('edit/ <int:id>', views.edit,name='edit'),  
     path('das/',views.das,name='das'),
     path('pro/',views.profile,name='profile'),
     path('chart/',views.chart,name='chart'),
     path('led/',views.led_control,name='led_control'),
     path('home/', views.INDEX, name='home'),
     path('add/', views.ADD, name='add'),
     path('demo/', views.ADDMORE, name='data'), 
     path('more/', views.adddata, name='adddata'),    
     path('ip/', ip_status, name='ip_status'),
  
     path('logout/',auth_views.LogoutView.as_view(template_name='app/front page.html'),name='logout'),
     
    
      
    
 
     




    #  path('check/', views.add_data, name='add_data'),
    
]