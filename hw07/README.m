1) Mapping from GP1_3 to GP1_4 using an interrupt 
was written in python and can be seen in the file
gpioInterrupt.py. The average delay was measured 
to be 720us.
2) Mapping using mmap was written in c and can be 
found in ./mmap/gpioMMAP.c.  The delay was measured 
to be 445ns.
3) Kernal mapping found in ./gpio_test/gpio_test.ko, 
but there were some issues so the delay was not measured.

