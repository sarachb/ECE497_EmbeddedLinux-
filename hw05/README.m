The LEDs cycle through GREEN-YELLOW-RED-OFF.
No matter what color the LED is set to, or if
it is off it will continue that patter.

The script must be run using sudo ./boneServer.js
To access the website to control the LED you must 
go to 192.168.7.2:9090 and click on Maxtrix LED.

Questions:
1)When "matrix" is sent to the bone, the bone itereates 
through the matrix array identifying if the index is send 
to green or not.  If it is set to greenthe LED displays 
green and if it isn't set, then the LED is off.

2) When an LED is clicked on the browser, the corresponging 
LED on the LED-Matrix updates its display to match the browser.  
This results each LED being able to toggle between green and off, 
while being controlled throgh the browser.

3)".on" is used to color the LED

4)To have the LEDs iterate through the GREEN-YELLOW-RED-OFF
pattern I will add a second array to represent the red LEDs.
If the green and red arrays are both "on" at the same index, 
then the maxtrix will display yellow. 

5) boneServer.js does not need to be changed.  


// Comments from Prof. Yoder
// It works, but is late
// Grade:  9/10
