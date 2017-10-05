#!/usr/bin/env pyton3
#Read a TMP101 sensor
# sudo apt install python3-smbus

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO



bus = smbus.SMBus(1)
address = 0x48
address2 = 0x4a

sensor = "GP1_4"
sensor2 = "GP1_3"
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(sensor2, GPIO.IN)

bus.write_byte_data(address, 3, 24) 
bus.write_byte_data(address2, 3, 24) 

map1 = {sensor: address, sensor2: address2}
map2 = {sensor: "TMP Sensor 1", sensor2:"TMP Sensor 2"}

def tempConvert(tmp):
    return round((tmp*1.8) + 32, 3)

def alertDetect(channel):
    alertAddr = map1[channel]
    alertSensor = map2[channel]
    temp = bus.read_byte_data(alertAddr, 0)
    print ("ALERT at " + str(alertSensor) + " with temperature: " + str(tempConvert(temp)) , end="\r")


GPIO.add_event_detect(sensor, GPIO.BOTH, callback = alertDetect)
GPIO.add_event_detect(sensor2, GPIO.BOTH, callback = alertDetect)
    


while True:
    temp = bus.read_byte_data(address, 0)
    temp2 = bus.read_byte_data(address2, 0)
    temp = tempConvert(temp)
    temp2 = tempConvert(temp2)
    print ("TMP Sensor 1: " + str(temp) + " TMP Sensor 2: " + str(temp2) , end= "\r")
    #print ("TMP Sensor 2: " + str(temp2) , end="\r")
    #print ("----------", end="\r")
    time.sleep(0.25)
    
    