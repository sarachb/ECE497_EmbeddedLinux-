// From : http://stackoverflow.com/questions/13124271/driving-beaglebone-gpio-through-dev-mem
//
// Read one gpio pin and write it out to another using mmap.
// Be sure to set -O3 when compiling.
// Modified by Mark A. Yoder  26-Sept-2013
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h> 
#include <signal.h>    // Defines signal-handling functions (i.e. trap Ctrl-C)
#include "beaglebone_gpio.h"

/****************************************************************
 * Global variables
 ****************************************************************/
int keepgoing = 1;    // Set to 0 when ctrl-c is pressed

/****************************************************************
 * signal_handler
 ****************************************************************/
void signal_handler(int sig);
// Callback called when SIGINT is sent to the process (Ctrl-C)
void signal_handler(int sig)
{
    printf( "\nCtrl-C pressed, cleaning up and exiting...\n" );
	keepgoing = 0;
}

int main(int argc, char *argv[]) {
    volatile void *gpio_addr;
    printf("1");
    volatile void *gpio_addr_led;
    volatile unsigned int *gpio_oe_addr_led;
    volatile unsigned int *gpio_datain_led;
    volatile unsigned int *gpio_setdataout_addr_led;
    volatile unsigned int *gpio_cleardataout_addr_led;
    
    volatile void *gpio_addr_btn;
    volatile unsigned int *gpio_oe_addr_btn;
    volatile unsigned int *gpio_datain_btn;
    volatile unsigned int *gpio_setdataout_addr_btn;
    volatile unsigned int *gpio_cleardataout_addr_btn;
    
    unsigned int reg;

    // Set the signal callback for Ctrl-C
    signal(SIGINT, signal_handler);

    int fd = open("/dev/mem", O_RDWR);

    printf("Mapping %X - %X (size: %X)\n", GPIO0_START_ADDR, GPIO0_END_ADDR, 
                                           GPIO0_SIZE);
    
    //led setup (gpio3_1 and gpio3_2)
    gpio_addr_led = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 
                        GPIO3_START_ADDR);

    gpio_oe_addr_led           = gpio_addr_led + GPIO_OE;
    gpio_datain_led            = gpio_addr_led + GPIO_DATAIN;
    gpio_setdataout_addr_led   = gpio_addr_led + GPIO_SETDATAOUT;
    gpio_cleardataout_addr_led = gpio_addr_led + GPIO_CLEARDATAOUT;

    //button setup (gpio1_25 and gpio1_17)
    gpio_addr_btn = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, 
                        GPIO1_START_ADDR);

    gpio_oe_addr_btn           = gpio_addr_btn + GPIO_OE;
    gpio_datain_btn            = gpio_addr_btn + GPIO_DATAIN;
    gpio_setdataout_addr_btn   = gpio_addr_btn + GPIO_SETDATAOUT;
    gpio_cleardataout_addr_btn = gpio_addr_btn + GPIO_CLEARDATAOUT;
    
    
    if(gpio_addr_led == MAP_FAILED | gpio_addr_btn == MAP_FAILED) {
        printf("Unable to map GPIO\n");
        exit(1);
    }
    printf("GPIO mapped to %p\n", gpio_addr_led);
    printf("GPIO OE mapped to %p\n", gpio_oe_addr_led);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr_led);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr_led);
    
    
    printf("GPIO mapped to %p\n", gpio_addr_btn);
    printf("GPIO OE mapped to %p\n", gpio_oe_addr_btn);
    printf("GPIO SETDATAOUTADDR mapped to %p\n", gpio_setdataout_addr_btn);
    printf("GPIO CLEARDATAOUT mapped to %p\n", gpio_cleardataout_addr_btn);

    printf("Start mapping GPIO1_25 to GPIO3_01 and GPIO1_17 to GPIO3_02\n");
    while(keepgoing) {
        
    	if (!(*gpio_datain_btn & GPIO1_25)) {
    	    *gpio_setdataout_addr_led= GPIO3_2;
    	} else {
            *gpio_cleardataout_addr_led = GPIO3_2;
    	}
    	
    	if ((*gpio_datain_btn & GPIO1_17)) {
    	    *gpio_setdataout_addr_led= GPIO3_1;
    	} else {
            *gpio_cleardataout_addr_led = GPIO3_1;
    	}
        usleep(1);
    }

    //munmap((void *)gpio_addr, GPIO0_SIZE);
    close(fd);
    return 0;
}
