import time
from machine import Pin
from lib.tm1637 import TM1637Decimal
tm = TM1637Decimal(clk=Pin("P11"), dio=Pin("P21"))

# maak een functie die ook verder kan tellen dan 9
# tip denk aan leading zero's
for i in range(10):
    tm.show("  "+ str(i))
    time.sleep(1)
