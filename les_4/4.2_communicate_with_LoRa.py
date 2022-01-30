from network import LoRa
import socket
import time
import ubinascii
import pycom

# To enable modification of the led
pycom.heartbeat(False)

RGB_RED = (0x7f0000)
RGB_GREEN = (0x007f00)
RGB_BLUE = (0X8)
RGB_YELLOW = (0x7f7f00)

# Make sure heartbeat is disabled before setting RGB LED
pycom.heartbeat(False)

# Initialise LoRa in LORAWAN mode.
lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

# set credentials -LoRa
app_eui = ubinascii.unhexlify('0000000000000000')
app_key = ubinascii.unhexlify('')

lora.join(activation=LoRa.OTAA, auth=(lora.mac(), app_eui, app_key), timeout=0)
print('trying to join TTN Network...')

while not lora.has_joined():
    pycom.rgbled(RGB_YELLOW)
    time.sleep(5)
    print('...')
    pass

print('network joined')
pycom.rgbled(RGB_BLUE)
# create a LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
# set the LoRaWAN data rate
s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

try:
    while lora.has_joined():
        s.setblocking(True)    
          
        # get message of a node (01, 02, 03, 04, 05, 06)        
        node = input("retrieve a message of node: ") 
        if node != "":       
            s.send(node)
                                      
            # waiting for a response
            s.setblocking(False)
            data = s.recv(64).decode()                
            print(data)        
            print("")
            time.sleep(1.0)           
   
except:
    print('Connection lost')
    pycom.heartbeat(False)