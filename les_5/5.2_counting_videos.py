'''kopieer de code van 5.1 en gebruik je oplossing uit 2.3 (segment)'''
'''tel het aantal videobanden dat de eerste keer wordt aangeboden (items in queue / voorraad)'''

from machine import Pin
from lib.tm1637 import TM1637Decimal
tm = TM1637Decimal(clk=Pin("P11"), dio=Pin("P21"))

counter = 1
digits = 4 - len(str(counter))
tm.show(("0" * digits) + str(counter))