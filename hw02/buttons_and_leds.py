import Adafruit_BBIO as GPIO
import time

LED0 = "LED_UP"
LED1 = "LED_DOWN"
LED2 = "LED_LEFT"
LED3 = "LED_RIGHT"
delay= 0.25

GPIO.setup(LED0, GPIO.OUT)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

buttonU = "UP"
buttonD = "DOWN"
buttonL = "LEFT"
buttonR = "RIGHT"


#Set up the GPIO pins:
GPIO.setup(buttonU, GPIO.IN)
GPIO.setup(buttonD, GPIO.IN)
GPIO.setup(buttonL, GPIO.IN)
GPIO.setup(buttonr, GPIO.IN)

#Turn on all  LEDs
#GPIO.output(LEDp, 1)
#GPIO.output(LEDm,. 1)

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
        time.sleep(100)
        
except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.clenup()



while True:
    GPIO.output(LED0, 1)
    time.sleep(delay)
    GPIO.sleep(LED0, 0)
    time.sleep(delay)
while True:
    GPIO.output(LED1, 1)
    time.sleep(delay)
    GPIO.sleep(LED1, 0)
    time.sleep(delay)
while True:
    GPIO.output(LED2, 1)
    time.sleep(delay)
    GPIO.sleep(LED2, 0)
    time.sleep(delay)
while True:
    GPIO.output(LED3, 1)
    time.sleep(delay)
    GPIO.sleep(LED3, 0)
    time.sleep(delay)