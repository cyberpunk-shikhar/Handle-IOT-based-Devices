from django.db import models

# Create your models here.

class User(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Password= models.CharField(max_length=50)
    
    def __str__(self):
        return self.Firstname
    
    
    
    
#arduino model.

class ArduinoData(models.Model):
    device_id = models.CharField(max_length=255)
    data = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

   
    
    
    
# class ArduinoData(models.Model):
#     temperature = models.DecimalField(max_digits=5, decimal_places=2)
#     humidity = models.DecimalField(max_digits=5, decimal_places=2)
#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Temperature: {self.temperature}, Humidity: {self.humidity}, Timestamp: {self.timestamp}"

    
    
# class ConsoleData(models.Model):
#     console_id =models.CharField(max_length=50)
#     data = models.CharField(max_length=255)
#     timestamp = models.DateTimeField(auto_now_add=True)    


 
# class COMPortLog(models.Model):
#     timestamp = models.DateTimeField(auto_now_add=True)
#     is_connected = models.BooleanField()


# appname/models.py
 


 # led_control_app/models.py



 #setting page model 
 
 
 

class DHTData(models.Model):
    temperature = models.CharField(max_length=255)
    humidity = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
 

 











    
    
    
    
    

class EMPLOYEES(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=180)
    address = models.TextField()
    phone = models.IntegerField()
    
    
    
class ADDDEVICES(models.Model):
    device_id = models.CharField(max_length=180)
    device_name = models.CharField(max_length=200)
    device_ip = models.GenericIPAddressField(blank=True, null=True)
    device_category = models.CharField(max_length=180)
    status = models.CharField(max_length=10, default='offline')
    
    def __str__(self):
        return self.device_ip











