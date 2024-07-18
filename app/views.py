from django.shortcuts import render,redirect,HttpResponse 
from .models import *
import serial,requests
import time
from .new import ArduinoDataForm 
from .models import ArduinoData 
from datetime import timezone
from datetime import datetime

from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages







def registerpage(request):
    return render(request,'app/register.html')


#signup view
def userregister(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        #first validate that user already exists
        user = User.objects.filter(Email=email)
        
        if user: 
            message = 'user already exists'
            return render(request,'app/register.html',{'msg':message})
        
        else:
            if password == cpassword:
                newuser = User.objects.create(Firstname=fname,Lastname=lname,Email=email,Contact=contact,Password=password)
                message = 'user register successfully'
                return render(request,'app/front page.html',{'msg':message})
    else:
        message = 'Passowrd and confirm passowrd does not match'
        return render(request,'app/register.html',{'msg':message})

#Login View
def Loginpage(request):
    return render(request,'app/front page.html')

def loginuser(request):
    if request.method == "POST":
        Email = request.POST.get('Email')
        Password = request.POST.get('password')
        
        try:
            user = User.objects.get(Email=Email)
        except User.DoesNotExist:
            message = 'User does not exist'
            return render(request, 'app/register.html', {'msg': message})

        if user.Password == Password:
            request.session['Firstname'] = user.Firstname
            request.session['Lastname'] = user.Lastname
            request.session['Email'] = user.Email
            return render(request, 'app/index.html')
        else:
            message = "Password does not match"
            return render(request, 'app/login.html', {'msg': message})

    # If the request method is not POST (e.g., GET request), render the login page
    return render(request, 'app/login.html')

                

def check_arduino_status(request ):
     ser = serial.Serial('COM3',9600) 
     data = ser.readline().decode().strip()
     arduino_data = ArduinoData(data=data)
     arduino_data.save()
     return render(request, 'app/Dlist.html',)

  
    
def store_arduino_data(request):
    arduinodata = ArduinoData.objects.all()
    ser = serial.Serial('COM3', 9600)  
    return render(request, 'app/tables.html',{'arduinodata':arduinodata}) 

 
def edit(request, id):  
        arduinodata  = ArduinoData.objects.get(id=id)  
        return render(request,'app/live_data.html', {'arduinodata':arduinodata})  
    
@login_required(login_url='/')
def das(request):
    return render(request,'app/index.html')



def profile(request):
    return render(request,'app/home.html')
     

def chart(request):
    arduinodata = ArduinoData.objects.all()
    context = {
        " arduinodata" :  arduinodata,
      }
    return render(request,'app/charts.html',{'arduinodata':arduinodata},)
     



# ESP32_IP = "192.168.137.176"  # Replace with your ESP32's IP address

# def led_control(request):
#     if request.method == 'POST':
        
#         if 'on' in request.POST:
#             requests.get(f"{ESP32_IP}/on")
#         elif 'off' in request.POST:
#             requests.get(f"{ESP32_IP}/off")
#         return render(request, 'app/led.html')

import requests

ESP8266_IP = "192.168.137.57"  # Replace with your ESP8266's IP address

def led_control(request):
    if request.method == 'POST':
        if 'on' in request.POST:
            requests.post(f"http://{ESP8266_IP}/?state=on")
            print("led on")
        elif 'off' in request.POST:
            requests.post(f"http://{ESP8266_IP}/?state=off")
            print("ledoff")
    return render(request, 'app/led.html')

  
      




def device(request):
       return render(request, 'app/device.html')


def esp32_ip_view(request):
    # Retrieve the ESP32 IP address from your database or variable
    
    esp32_ip = "192.168.137.228"  # Replace with the actual IP address
    return render(request, 'app/ip.html', {'esp32_ip': esp32_ip})


def sensor_data(request):
    sensor_data = DHTData.objects.all()
    # sensor_data.save()
    return render(request, 'app/dht.html', {'sensor_data': sensor_data})






    







#------add devices--------

def INDEX(request):
    emp = EMPLOYEES.objects.all()
    
    context ={
        'emp':emp,
    }
    return render(request, 'app/employees.html',context)

def ADD(request):
    if request.method == "POST":
        name =request.POST.get('name')
        email =request.POST.get('email')
        address =request.POST.get('address')
        phone =request.POST.get('phone')
        
        emp = EMPLOYEES(
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
    return redirect('home')


def ADDMORE(request):
    adm = ADDDEVICES.objects.all()
    
    contexts={
        'adm':adm,
    }
    return render(request, 'app/adddata.html',contexts)

def adddata(request):
    if request.method == "POST":
        device_id = request.POST.get('device_id')
        device_name = request.POST.get('device_name')
        device_ip = request.POST.get('device_ip')
        device_category = request.POST.get('device_category')

        # check duplicate ip
        isIpExist = ADDDEVICES.objects.filter(device_ip=device_ip).exists()

        print("isIpExist", isIpExist)
        if isIpExist is False:
            adm = ADDDEVICES(
                device_id = device_id,
                device_name = device_name,
                device_ip = device_ip,
                device_category = device_category,
            )
            adm.save()
        else:
            messages.error(request, "Ip Already exist")
            
    return redirect('data')



# def esp8266_status(request, device_id):
#     try:
#         device = ESP8266Device.objects.get(pk=device_id)
     
#         is_connected =  device_id

#         device.connected = device_id
#         device.save()

#         return render(request, 'app/status.html', {'device': device})
#     except ESP8266Device.DoesNotExist:
#         # return JsonResponse({'ERROR':'NOT VALID'})
#         return render(request, 'app/status.html')




# views.py
from django.shortcuts import render

import subprocess

def ping_ip(ip_address):
    try:
        subprocess.check_output(["ping", "-n", "1", ip_address])
        return True  # Ping successful
    except subprocess.CalledProcessError:
        return False  # Ping failed
def ip_status(request):
    ip_addresses = ADDDEVICES.objects.all()
    
    results = {}
    for ip in ip_addresses:
        status = ping_ip(ip.device_ip)
        results[ip.device_ip] = status
        
        # Update the status in the database
        devices = ADDDEVICES.objects.filter(device_ip=ip.device_ip)
        for device_instance in devices:
            device_instance.status = status
            device_instance.save()
    
    # Create a JsonResponse from the results dictionary
    return JsonResponse(results)

    # def update_device_status(request):
    #  ip = ADDDEVICES.get_deferred_fields('status')
    #  print(ip)

    # for ADDDEVICES in status :
    #     new_status = ping_ip(ip)
    #     if ADDDEVICES.status != new_status:
    #         ADDDEVICES.status = new_status
    #         ADDDEVICES.save()
         


    return render(request, 'app/results.html', {'results': results})






# views.py

