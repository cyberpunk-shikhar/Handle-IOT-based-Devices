from django.urls import path
from .import views


urlpatterns = [
    path('device1/', views.display_charts, name='index'),
    path('temp/<int:device_id>/', views.displayTemperatures,name='displayTemperatures'),
    path('hum/<int:device_id>/', views.displayHumidity,name='displayHumidity'),
    # path('bright/', views.displayBrightness,name='displayBrightness'),
    path('display_brightness/<int:device_id>/', views.displayBrightness, name='display_brightness'),

    path('pressure/<int:device_id>/', views.displayPressure,name='displayPressure'),


    
    
]
