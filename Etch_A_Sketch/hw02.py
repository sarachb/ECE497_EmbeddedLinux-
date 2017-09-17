#!user/bin/env python3

import pygame, sys
from pygame.locals import *
import Adafruit_BBIO as GPIO
import time

LED0 = "LED_UP"
LED1 = "LED_DOWN"
LED2 = "LED_LEFT"
LED3 = "LED_RIGHT"
delay= 0.25

GPI1.setup(LED0, GPIO.OUT)
GPI1.setup(LED1, GPIO.OUT)
GPI1.setup(LED2, GPIO.OUT)
GPI1.setup(LED3, GPIO.OUT)

#buttonP = "PAUSE" #PAUSE or MODE
#buttonM = "MODE"

buttonU = "UP"
buttonD = "DOWN"
buttonL = "LEFT"
buttonR = "RIGHT"

#LEDp = "RED"
#LEDm = "GREEN"

#Set up the GPIO pins:
#GPIO.setup(LEDp, GPIO.OUT)
#GPIO.setup(LEDm, GPIO.OUT)
GPIO.setup(buttonU, GPIO.IN)
GPIO.setup(buttonD, GPIO.IN)
GPIO.setup(buttonL, GPIO.IN)
GPIO.setup(buttonr, GPIO.IN)

#Turn on both LEDs
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


#GPI0=setup(LED0, GPIO.OUT)
#GPI1=setup(LED1, GPIO.OUT)
#GPI2=setup(LED2, GPIO.OUT)
#GPI3=setup(LED3, GPIO.OUT)

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


    

pygame.init()

screen = pygame.display.set_mode(600,400)
x=300
y=200

clock=pygame.time.Clock()
screen.fill((255,255,255))

while 1:
    clock.tick(60)
    pygame.draw.circle(screen, (0,0,0), (x,y), 2)
    pygame.display.update()
    key = pygame.key.get_pressed()
    if key[pygame.K_RIGHT]: x+= 1
    if key[pygame.K_LEFT]: x-=1
    if key[pygame.K_UP]: y-=1
    if key[pygame.K_DOWN]: y+=1
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            sys.exit()
        elif event.type == KEYDOWN and event.key == K_SPACE:
            screen.fill((255,255,255))
            
            
        
