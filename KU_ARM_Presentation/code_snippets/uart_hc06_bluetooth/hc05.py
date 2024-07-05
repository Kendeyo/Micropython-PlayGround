# import Pin and UART classes
from machine import Pin, UART

uart0 = UART(0,9600) 		#create an object of UART 0 and initialize with 9600 baudrate
led = Pin(25, Pin.OUT)		#create an led object
led.value(0)				#initially the led is set OFF

uart0.write("welcome to this event \r\n")

while True:
    if uart0.any() > 0:                #read if there is any value being received
        data = uart0.read(1)			#create a variable and store the received data
        if "a" in data:
            led.value(1)
            uart0.write("LED ON \r\n")
        elif "b" in data:
            led.value(0)
            uart0.write("LED OFF \r\n")