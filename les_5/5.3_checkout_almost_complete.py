'''combineer onderstaande code met de code van 5.2
   en pas de printfunctie alsvolgt aan 
   eerste keer aanbieden - received: title_dvd 
   tweede keer aanbieden - send: title_dvd'''

            # requesting title
            print('requesting title DVD')                    
            s.send(uid)
            print("")
                    
            # waiting for a response
            print('listening for a response')
            s.setblocking(False)
            data = ""
            while data == "":          
                data = s.recv(64).decode()
            print(data)

            time.sleep(2)

            print("")

from network import LoRa
from MFRC630 import MFRC630
from pycoproc_1 import Pycoproc
import socket
import time
import ubinascii
import pycom

# To enable modification of the led
pycom.heartbeat(False)

py = Pycoproc(Pycoproc.PYSCAN)
nfc = MFRC630(py)

RGB_RED = (0x7f0000)
RGB_GREEN = (0x007f00)
RGB_BLUE = (0X8)
RGB_YELLOW = (0x7f7f00)

# Make sure heartbeat is disabled before setting RGB LED
pycom.heartbeat(False)

# Initialise the MFRC630 with some settings
nfc.mfrc630_cmd_init()

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
print('scanning for videos')

try:
    while lora.has_joined():
        s.setblocking(True)    
        atqa = nfc.mfrc630_iso14443a_WUPA_REQA(nfc.MFRC630_ISO14443_CMD_REQA)
        if (atqa != 0):        
        	# A card has been detected, read UID
            print('A video has been detected, reading its UID ...')
            uid = bytearray(7)
            uid_len = nfc.mfrc630_iso14443a_select(uid)
            
            if nfc.format_block(uid, uid_len) != "":
                print(str(nfc.format_block(uid, uid_len)))             


            else:
                print('unable to determine its UID, try again')             

            time.sleep(2)
            print('Scanning for products') 
        else:
            pycom.rgbled(RGB_BLUE)

except:
    print('Connection lost')
    pycom.heartbeat(False)
    nfc.mfrc630_cmd_reset()
    time.sleep(.5)    
    nfc.mfrc630_cmd_init()
