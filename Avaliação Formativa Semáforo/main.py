import machine 
import time

led1 = machine.Pin(14, machine.Pin.OUT)

led2 = machine.Pin(27, machine.Pin.OUT)

led3 = machine.Pin(26, machine.Pin.OUT)

while True:
    led1.value(1)
    time.sleep(5)
    led1.value(0)

    led2.value(1)
    time.sleep(3)
    led2.value(0)
   
    led3.value(1)
    time.sleep(5)
    led3.value(0)
   




