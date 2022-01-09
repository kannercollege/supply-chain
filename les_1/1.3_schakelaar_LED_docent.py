from machine import Pin
import time
led = Pin('P9', mode = Pin.OUT)
button = Pin('P10', mode = Pin.IN, pull=Pin.PULL_UP)

while True:
    if(button() == 0):
        led.value(1)
        print("low")
                
    else:
        led.value(0)
        print("high")
       
    time.sleep(1)