#!/usr/bin/env/ python3
import Adafruit_BBIO.GPIO as GPIO
import time

LED0 = "USR1"
LED1 = "USR2"
LED2 = "USR3"
LED3 = "USR0"
#delay= 0.25


buttonU = "GP0_4"
buttonD = "GP0_5"
buttonL = "GP0_6"
buttonR = "GP0_3"


GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

#Set up the GPIO pins:
GPIO.setup(buttonU, GPIO.IN)
GPIO.setup(buttonD, GPIO.IN)
GPIO.setup(buttonL, GPIO.IN)
GPIO.setup(buttonr, GPIO.IN)

#Turn on all  LEDs
GPIO.output(LED0, 1)
GPIO.output(LED1, 1)
GPIO.output(LED2, 1)
GPIO.output(LED3, 1)


#Map buttons to LEDs
map = {buttonU:LED0, buttonD:LED1, buttonL:LED2, buttonR:LED3}

def updateLED(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print(map[channel] + " Toggled")
    
print("Running....")

GPIO.add_event_detect(buttonU, GPIO.BOTH, callback = updateLED)
GPIO.add_event_detect(buttonD, GPIO.BOTH, callback = updateLED)
GPIO.add_event_detect(buttonL, GPIO.BOTH, callback = updateLED)
GPIO.add_event_detect(buttonR, GPIO.BOTH, callback = updateLED)

try:
    while True:
        time.sleep(0.25)
        
except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()




#while True:
#    GPIO.output(LED0, 1)
#    time.sleep(delay)
#    GPIO.sleep(LED0, 0)
#    time.sleep(delay)
#while True:
#    GPIO.output(LED1, 1)
#    time.sleep(delay)
#    GPIO.sleep(LED1, 0)
#    time.sleep(delay)
#while True:
#    GPIO.output(LED2, 1)
#    time.sleep(delay)
#   GPIO.sleep(LED2, 0)
#    time.sleep(delay)
#while True:
#    GPIO.output(LED3, 1)
#    time.sleep(delay)
#    GPIO.sleep(LED3, 0)
#    time.sleep(delay)
