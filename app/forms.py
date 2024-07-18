import serial
import time


# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

 
while True:
    line = ser.readline()   # read a byte
    #print(line)
    if line:
        string = line.decode().strip()  # convert the byte string to a unicode string
        #num = int(string) # convert the unicode string to an int
        print(string)



    



# import machine
# import adafruit_dht
# import urequests
# import time

# # Define the sensor and pin
# dht_sensor = adafruit_dht.DHT11(machine.Pin(4))  # Replace 4 with the actual GPIO pin number
# server_url = 'http://127.0.0.1:8000/'  # Replace with your Django server URL

# while True:
#     try:
#         dht_sensor.measure()
#         temperature_celsius = dht_sensor.temperature()
#         humidity_percent = dht_sensor.humidity()

#         data = {'temperature': temperature_celsius, 'humidity': humidity_percent}
#         response = urequests.post(server_url, json=data)
#         response.close()
        
#         print("Data sent to server.")
#     except Exception as e:
#         print("Error:", e)
    
#     time.sleep(60)  # Send data every minute (adjust as needed)

    



