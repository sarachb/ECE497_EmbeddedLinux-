#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

buttonU = "GP0_3"
buttonD = "GP0_4"
buttonL = "GP0_6"
buttonR = "GP0_5"

#Set up the GPIO pins:
GPIO.setup(buttonU, GPIO.IN)
GPIO.setup(buttonD, GPIO.IN)
GPIO.setup(buttonL, GPIO.IN)
GPIO.setup(buttonR, GPIO.IN)


count = 10
#colCount = 10

x = 0
y = 0



table = [[" " for j in range(count)] for i in range (count)]




  
    
def updateTable(channel):
    global count
    
    global x
    global y
    global table
    
    print (x)
    print (y)
    if (channel == "GP0_5") & (y < (count -1)): #right 
        y = y + 1
    elif (channel == "GP0_3") & ( x > 0): #up
        x = x-1
    elif (channel == "GP0_4") & (x < (count -1)): #down
        x = x +1
    elif (channel == "GP0_6") & (y > 0): #left
        y = y-1
        
    table[x][y] = "O"
    
    for i in range(0, count):
        print(table[:][i])
    print ("BUTTON PRESSED")
    
    
    
        
    

def sketch(channel):
    global count
    
    global x
    global y
    
    for x in range(count):
        for y in range(count):
            table[x][y] = ""
    
    for y in range(count):
        print (table[:][y])
    x =0
    y=0


for y in range(count):
    print (table[:][y])
    

GPIO.add_event_detect(buttonU, GPIO.BOTH, callback = updateTable)
GPIO.add_event_detect(buttonD, GPIO.BOTH, callback = updateTable)
GPIO.add_event_detect(buttonL, GPIO.BOTH, callback = updateTable)
GPIO.add_event_detect(buttonR, GPIO.BOTH, callback = updateTable)

try:
    while True:
        time.sleep(0.25)
        
except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
GPIO.cleanup()

    
    
    
    
    