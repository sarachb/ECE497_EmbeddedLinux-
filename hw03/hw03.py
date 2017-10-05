#!/usr/bin/env pyton3
#Read a TMP101 sensor
# sudo apt install python3-smbus

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

bus = smbus.SMBus(1)
matrix = 0x70
temp1 = 0x49
temp2 = 0x4a
delay = 0.25


#buttons
buttonU = "GP0_4"
buttonD = "GP0_5"
buttonL = "GP0_6"
buttonR = "GP0_3"

GPIO.setup(buttonU, GPIO.IN)
GPIO.setup(buttonD, GPIO.IN)
GPIO.setup(buttonL, GPIO.IN)
GPIO.setup(buttonR, GPIO.IN)


#temp sensors
sensor = "GP1_4"  #if detected clear  the board 
sensor2 = "GP1_3" #if detected start game 
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(sensor2, GPIO.IN)


count = 8
# x=0
# y=0
x=0x01
y=0x00

smile = [0x00, 0x3c, 0x00, 0x42, 0x28, 0x89, 0x04, 0x85,
0x04, 0x85, 0x28, 0x89, 0x00, 0x42, 0x00, 0x3c
]

etch = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]

clear = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]


# Start oscillator (p10)
bus.write_byte_data(matrix, 0x21, 0)
# Disp on, blink off (p11)
bus.write_byte_data(matrix, 0x81, 0)
# Full brightness (page 15)
bus.write_byte_data(matrix, 0xe7, 0)

bus.write_i2c_block_data(matrix, 0, smile)

# bus.write_byte_data(temp1, 3, 24) 
# bus.write_byte_data(temp2, 3, 24) 

map1 = {sensor: temp1, sensor2: temp2}
start = True
#clear = True

def drawTable(grid):
    global matrix
   
    
    bus.write_i2c_block_data(matrix, 0, grid)
    
def updateTable(channel):
    global count
    global x
    global y
    global start
    
    print ("BUTTON PRESSED")
    print (etch)
    print (x)
    print(y)
    
    if (((channel == "GP0_5") | (channel == "GP0_6") | (channel == "GP0_4") | (channel == "GP0_3")) & ( start == True)):
        drawTable(etch)
        start = False
        print ("Start by going right! Press Button 5")
    elif (channel == "GP0_5") & ( x > 0x01):#(y < (count)): #right 
        print("right")
        x = x >> 1
        #if (y + 1)< (count): y = y+1
    elif (channel == "GP0_3") & (y < 15):#( x > 1): #up
        print("up")
        y = y +2
        #if (x+1)> 0: x = x+1
    elif (channel == "GP0_4") & (y > 0):#(x < (count)): #down
        print("down")
        y = y -2
        #if (x -1)< (count) : x= x-1
    elif (channel == "GP0_6") & (x < 0x80):#(y > 1): #left
        print("left")
        x = x << 1
        #if (y-1) > 0: y=y-1
    
        
    # ref= (2*x) -1
    # etch[ref] = etch[ref] | 0x01 << (count-y)
    etch[y] = etch[y] | x
    
    drawTable(etch)
    
    
    
        
  
   
    
# def alertDetect(channel):
#     alertAddr = map1[channel]
#     temp = bus.read_byte_data(alertAddr, 0)
#     #print (temp)
#     if (channel == "GP1_3") & (temp >= 27):
#         print ("Etch")
#         bus.write_i2c_block_data(matrix, 0, etch)
#     if (channel == "GP1_4") & (temp >= 27):
#         print ("Clear")
#         bus.write_i2c_block_data(matrix, 0, clear)
    
    
    


# GPIO.add_event_detect(sensor, GPIO.BOTH, callback = alertDetect)
#GPIO.add_event_detect(sensor2, GPIO.BOTH, callback = alertDetect)

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