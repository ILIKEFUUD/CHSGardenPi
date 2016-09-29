"""
Rahul Shah
PD 6 Internship with Mr. Sell

monitor.py

Using the Raspberry Pi, monitor the moisture, temperature, and light being given to the plant system
"""

import grovepi
import time

#Sensor connected to A0 Port
sensor = 14             # Pin 14 is A0 Port.

#Sensor connected to D7 port
dht_sensor_port = 7
grovepi.pinMode(sensor,"INPUT")

while True:
    try:

        #temperature
        [temp,hum] = grovepi.dht(dht_sensor_port, 1) #get temp and hum
        temp /= 10.0
        print("Temperature: %f" %temp)
        time.sleep(.5)

        #light
        sensor_value = grovepi.analogRead(sensor)

        print ("sensor_value = %d" %sensor_value)
        time.sleep(.5)

    except IOError:
        print ("Error")

        






