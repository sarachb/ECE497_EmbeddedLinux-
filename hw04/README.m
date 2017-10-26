GPIO with MMAP:
Button Mapping: GPIO1 port
LED Mapping: GPIO3 port

To run: 
For ports 97 and 98
1)echo "port" > export
2) if cat direction outputs in 
    a) echo out direction

3) gcc -o temp gpioThru.c
4) ./temp

Rotary Encoder:
The right encoder represent the directions UP and DOWN
by turning it left or right, respectively.
The left enconder represent the LEFT and RIGHT, but 
turning the enconcer left or right, respectively.

To run: python3 hw04.py
This runs only if you have rcpy installed

// Comments from Prof. Yoder
// Memory Map info is missing.
// It works!
// Grade:  8/10
