#!/usr/bin/env pyton3
#Read a TMP101 sensor
# sudo apt install python3-smbus

import smbus
import time
import Adafruit_BBIO.GPIO as GPIO

# import rcpy library
# This automatically initizalizes the robotics cape
import rcpy 
import rcpy.encoder as encoder
bus = smbus.SMBus(1)
matrix = 0x70
temp1 = 0x49
temp2 = 0x4a
delay = 0.25

count = 8
# x=0
# y=0
x=0x01
y=0x00

#smile face for start
smile = [0x00, 0x3c, 0x00, 0x42, 0x28, 0x89, 0x04, 0x85,
0x04, 0x85, 0x28, 0x89, 0x00, 0x42, 0x00, 0x3c
]

#game
etch = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00
]


# Start oscillator (p10)
bus.write_byte_data(matrix, 0x21, 0)
# Disp on, blink off (p11)
bus.write_byte_data(matrix, 0x81, 0)
# Full brightness (page 15)
bus.write_byte_data(matrix, 0xe7, 0)

#wirting smiley face to the matrix
bus.write_i2c_block_data(matrix, 0, smile)


rcpy.set_state(rcpy.RUNNING)
print("Press Ctrl-C to exit")

# header
print('     E2 |     E3')
try:
    # keep running
    startE2 = 0
    startE3 = 0
    
    
    
    while True:
        # running
        if rcpy.get_state() == rcpy.RUNNING:
            e2 = encoder.get(2) # read the encoders
            e3 = encoder.get(3)
            print('\r {:+6d} | {:+6d}'.format(e2,e3), end='')
        time.sleep(.1)  # sleep some
        if ((e2 != startE2) | (e3 != startE3)):
            bus.write_i2c_block_data(matrix, 0, etch)
            if (e2 != startE2):
                if (e2 > startE2) & ( x > 0x01):
                    print (" ==> Direction: Right")
                    x = x >> 1
                elif (e2 < startE2) & (x < 0x80):
                    print (" ==> Direction: Left")
                    x = x << 1
                startE2 = e2
            elif (e3 != startE3):
                if (e3 > startE3) & (y < 15):
                    print (" ==> Direction: Up")
                    y= y + 2
                elif (e3 < startE3) & (y >0):
                    print (" ==> Direction: Down")
                    y = y-2
                startE3 = e3
            etch[y] = etch[y] | x
            bus.write_i2c_block_data(matrix, 0, etch)
                
                

except KeyboardInterrupt:
    # Catch Ctrl-C
    pass

finally:
    print("\nBye BeagleBone!")



