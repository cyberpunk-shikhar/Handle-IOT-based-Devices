from django.shortcuts import render
from django.utils import timezone
from django.db.models import Count,F,Sum,Avg
from django.db.models.functions import ExtractYear,ExtractMonth
from django.http import JsonResponse
from api_app.models import MeasurementItem
from .utils import (
    colorDanger, colorPalette,
    colorPrimary,colorSuccess,
    generate_color_palette)
# Create your views here.

def display_charts(request):
    return render(request,'charts.html', {})


def displayHumidity(request,device_id):

    local_tz = timezone.get_current_timezone() 

    temp_hum = MeasurementItem.objects.filter(device_id=device_id)
    

    def find_unique_device_ids(queryset):
    # Using set to store unique device_ids
        unique_device_ids = set()

        for item in queryset:
            unique_device_ids.add(item.device_id)

        return list(unique_device_ids)

# Call the function with your queryset
    unique_device_ids_list = find_unique_device_ids(temp_hum)

# Now unique_device_ids_list contains unique 'device_id' values from the temp_hum queryset
    print(unique_device_ids_list)

    humidityList = MeasurementItem.objects.filter(device_id=device_id).values_list('humidity',flat=True)
    timestampList = MeasurementItem.objects.filter(device_id=device_id).values_list('timestamp',flat=True)
    deviceid = MeasurementItem.objects.values_list('device_id')
  
    

    numElements = len(humidityList)

    hList = []
    tsList = []
    dList = []

    for id in range(numElements):
        hList.append(float(humidityList[id]))
        dList.append(float(deviceid[id][0]))
        # print(dList)

    for id in range(numElements):

        timestampFromDb = timestampList[id]
        datetimeLocal = timestampFromDb.astimezone(local_tz)
        timestamp = str(datetimeLocal)

        timestamp = timestamp.split('.')[0]
        tsList.append(timestamp)

    return JsonResponse({
        'title' : f'Humidity for Device ID {device_id}',
        'data': {
            'labels': tsList,
            'datasets': [{
                'label': 'Humidity (%)',
                'backgroundColor': generate_color_palette(1),
                'borderColor': generate_color_palette(numElements),
                'data': hList,
                'List': dList,
            }]
        },
    }    )


def displayTemperatures(request,device_id):

    local_tz = timezone.get_current_timezone()

    temp_hum = MeasurementItem.objects.filter(device_id=device_id)
    temperaturesList = MeasurementItem.objects.filter(device_id=device_id).values_list('temperature',flat=True)

    timestampList = MeasurementItem.objects.filter(device_id=device_id).values_list('timestamp',flat=True)

    numElements = len(temperaturesList)

    tList = []

    tsList = []

    for id in range(numElements):
        tList.append(float(temperaturesList[id]))



    for id in range(numElements):
        timestampFromDb = timestampList[id]
        datetimeLocal = timestampFromDb.astimezone(local_tz)
        timestamp = str(datetimeLocal)
        
        timestamp = timestamp.split('.')[0]
        tsList.append(timestamp)



    return JsonResponse({
        'title' : f'Temperature for Device ID{device_id}',
        'data': {
            'labels': tsList,
            'datasets': [{
                'label': 'Temperature (°C)',
                'backgroundColor': colorPalette[2],
                'borderColor': generate_color_palette(numElements),
                'data': tList,
            }]
        },
    }    )


def displayBrightness(request,device_id):

    local_tz = timezone.get_current_timezone()

    temp_hum = MeasurementItem.objects.filter(device_id=device_id)
    
    def find_unique_device_ids(queryset):
        unique_device_ids = set()

        for item in queryset:
            unique_device_ids.add(item.id)

        return list(unique_device_ids)


    u_list = find_unique_device_ids(temp_hum)
    print(u_list)

  
    brightnessList = MeasurementItem.objects.filter(device_id=device_id).values_list('brightness',flat=True)
    timestampList = MeasurementItem.objects.filter(device_id=device_id).values_list('timestamp',flat=True)

    numElements = len(brightnessList)

    bList = []
    tsList = []
    u_list =[]


    for id in range(numElements):
        bList.append(float(brightnessList[id]))

    for id in range(numElements):
        timestampFromDb = timestampList[id]
        datetimeLocal = timestampFromDb.astimezone(local_tz)
        timestamp = str(datetimeLocal)

        timestamp = timestamp.split('.')[0]
        tsList.append(timestamp)

    return JsonResponse({
        'title' : f'Brightness for Device ID {device_id}',
        'data': {
            'labels': tsList,
            'datasets': [{
                'label': 'Brightness (lx)',
                'backgroundColor': colorPalette[3],
                'borderColor': generate_color_palette(numElements),
                'data': bList,
            }]
        },
    }    )


def displayPressure(request,device_id):

    local_tz = timezone.get_current_timezone()

    temp_hum = MeasurementItem.objects.filter(device_id=device_id)
    pressuresList = MeasurementItem.objects.filter(device_id=device_id).values_list('atmosphericPressure',flat=True)
    timestampList = MeasurementItem.objects.filter(device_id=device_id).values_list('timestamp',flat=True)

    numElements = len(pressuresList)

    pList = []
    tsList = []

    for id in range(numElements):
        pList.append(float(pressuresList[id]))

    for id in range(numElements):
        timestampFromDb = timestampList[id]
        datetimeLocal = timestampFromDb.astimezone(local_tz)
        timestamp = str(datetimeLocal)

        timestamp = timestamp.split('.')[0]
        tsList.append(timestamp)

    return JsonResponse({
        'title' : f'Atmospheric pressure{device_id}',
        'data': {
            'labels': tsList,
            'datasets': [{
                'label': 'Atmospheric pressure (hPa)',
                'backgroundColor': colorPalette[6],
                'borderColor': generate_color_palette(numElements),
                'data': pList,
            }]
        },
    }    )