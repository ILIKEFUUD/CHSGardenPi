"""
Rahul Shah

PD 6 Internship with Mr. Sell

monitor.py

Using the Raspberry Pi, monitor the moisture, temperature, and light being given to the plant system
"""
import subprocess
import grovepi
import time
import requests
import sys
from grove_rgb_lcd import *


#pi land settings
room = 240
slot_light = 30
name_light = "Lamp+Light"

slot_temp = 22
name_temp = "Inside+Temp+DHT22"

slot_moisture = 24
name_moisture = "Soil+Moisture"

#Sensor connected to A0 Port
sensor = 14             # Pin 14 is A0 Port.
sensor_moist = 1              # Soil Moisture in port A1
#Sensor connected to D7 port
dht_sensor_port = 7
grovepi.pinMode(sensor,"INPUT")


#url variables
baseurl = "http://piland.socialdevices.io"
light_baseurl = baseurl + "/" + str(room) + "/write/" + str(slot_light) + "?name=" + name_light + "&value="
temp_baseurl = baseurl + "/" + str(room) + "/write/" + str(slot_temp) + "?name=" + name_temp + "&value="
moisture_baseurl = baseurl + "/" + str(room) + "/write/" + str(slot_moisture) + "?name=" + name_moisture + "&value="

while True:
    try:
        
        #moisture
        moisture_value = grovepi.analogueRead(sensor_moist)
        moistStr = "Soil Moisture: %d Moisture Meters" %moisture_value
        print(moistStr)
        
        #temperature
        [temp,hum] = grovepi.dht(dht_sensor_port, 1) #get temp and hum
        temp /= 10.0
        tempStr = "Temp: %.2f *C" %temp
        print(tempStr)


        #light
        sensor_value = grovepi.analogRead(sensor)
        lightStr = "Light: %d lux" %sensor_value

        print(lightStr)
        light_url = light_baseurl + "%0.1f" % sensor_value + "+lux"
        temp_url = temp_baseurl + "%0.1f" % temp + "+C"
        moisture_url = moisture_baseurl + "%0.1f" % moisture_value + "Moisture Meters"
        
        requests.get(light_url)
        requests.get(temp_url)
        requests.get(moisture_url)
        
        setText(tempStr)
        setRGB(0,128,64)
        time.sleep(1)
        setText(lightStr)
        setRGB(128,64,0)
        time.sleep(1)
        setText(moistStr)
        
        #when button pushed, shutdown
        if(grovepi.digitalRead(button) == 1):
            #subprocess.call("sudo shutdown -h now", shell = True)
            setText("Shutting down...")
            setRGB(0,0,0)
            setText("")

    except KeyboardInterrupt:
        print "Terminating"
        break
    except IOError:
        print "IOError, continuing"
    except:
        print "Unexpected error, continuing"
        print "sys.exc_info()[0]: ", sys.exc_info()[0]

