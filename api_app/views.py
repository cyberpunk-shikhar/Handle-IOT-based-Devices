from django.shortcuts import get_object_or_404,render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MeasurementItemSerializer
from .models import MeasurementItem 
from django.db.models import Count,F,Sum,Avg
from django.db.models.functions import ExtractYear,ExtractMonth


class MeasurementItemViews(APIView):

    def get(self, request, id=None):
        if id:
            item = MeasurementItem.objects.get(id=id)
            serializer = MeasurementItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = MeasurementItem.objects.all()
        serializer = MeasurementItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MeasurementItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        item = MeasurementItem.objects.get(id=id)
        serializer = MeasurementItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        item = get_object_or_404(MeasurementItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})



# <--------- start---search by device id-------------------->    
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import MeasurementItem

def fetch_data_by_device_id(request, device_id):
    # Query the database to fetch data for the given device_id
    measurements = MeasurementItem.objects.filter(device_id=device_id)

    # You can customize how you want to serialize the data
    data = {
        'measurements': [
            {
                'temperature': measurement.temperature,
                'humidity': measurement.humidity,
                'brightness': measurement.brightness,
                'atmosphericPressure': measurement.atmosphericPressure,
                'timestamp': measurement.timestamp,
            }
            for measurement in measurements
        ]
    }

    return JsonResponse(data)


# <--------end here--------->




def demo_data(request):

    table = MeasurementItem.objects.all()
    print(table)

    contexts={
        'table': table,
    }
    return render(request, 'data_table.html',contexts)