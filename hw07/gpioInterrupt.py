#!/usr/bin/env pyton3


import time
import Adafruit_BBIO.GPIO as GPIO

port4 = "GP1_4"
port3 = "GP1_3"

GPIO.setup(port4, GPIO.OUT)
GPIO.setup(port3, GPIO.IN)


portMap = {port3:port4}
print ("port mapped")

def alertDetect(channel):
    # print ("ALERT!")
    state = GPIO.input(channel)
    GPIO.output(portMap[channel], state)
    


GPIO.add_event_detect(port3, GPIO.BOTH, callback = alertDetect)

try:
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    print("Cleaning up")
    GPIO.cleanup()
    
GPIO.cleanup()
