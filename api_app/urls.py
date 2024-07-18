from django.urls import path
from .views import MeasurementItemViews
from . import views


urlpatterns = [
    path('measurement-items/', MeasurementItemViews.as_view()),
    path('measurement-items/<int:id>', MeasurementItemViews.as_view()),
    path('fetch-data/<str:device_id>/', views.fetch_data_by_device_id, name='fetch_data_by_device_id'),
    path('tb_demo/', views.demo_data,name='tb_demo'),
]
