from lib.Matrix8x8 import Matrix8x8
from machine import SPI, Pin
import time, math

clk = "P9"
din = "P10"
spi = SPI(0, baudrate=10000000, polarity=1, pins=(clk, din, None))
cs = Pin("P21", Pin.OUT)       

def print_on_matrix(text):
    msg = text
    length = len(msg)
    length = (length*8)
    display = Matrix8x8(spi, cs, 4)
    display.brightness(1)   # adjust brightness 1 to 15
    display.fill(1)
    display.show()
    time.sleep(0.5)
    display.fill(0)
    display.show()
    time.sleep(0.2)

    for x in range(32, -length, -1):
        display.text(msg ,x,0,1)
        display.show()
        time.sleep(0.10)
        display.fill(0)