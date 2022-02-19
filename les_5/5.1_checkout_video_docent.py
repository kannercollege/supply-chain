from MFRC630 import MFRC630
from pycoproc_1 import Pycoproc
import time
import pycom
import json

py = Pycoproc(Pycoproc.PYSCAN)
nfc = MFRC630(py)

RGB_RED = (0x7f0000)
RGB_GREEN = (0x007f00)
RGB_BLUE = (0X8)
RGB_ORANGE = (0x7f1f00)
RGB_YELLOW = (0xffc000)

# Make sure heartbeat is disabled before setting RGB LED
pycom.heartbeat(False)

# Initialise the MFRC630 with some settings
nfc.mfrc630_cmd_init()
print('Scanning for videos')
try:
    while True:
        # Send REQA for ISO14443A card type
        atqa = nfc.mfrc630_iso14443a_WUPA_REQA(nfc.MFRC630_ISO14443_CMD_REQA)
        if (atqa != 0):
        	# A card has been detected, read UID
            print('A video has been detected, reading its UID ...')
            uid = bytearray(7)
            uid_len = nfc.mfrc630_iso14443a_select(uid)        

            if nfc.format_block(uid, uid_len) != "":
                print(str(nfc.format_block(uid, uid_len)))
                    
                with open("inventory.json", "r") as f:
                    data = json.load(f)
            
                for index, value in enumerate(data):
                    if value == nfc.format_block(uid, uid_len).rstrip():
                        data.remove(value)
                        pycom.rgbled(RGB_ORANGE)
                        break
                else:            
                    data.append(nfc.format_block(uid, uid_len).rstrip())
                    pycom.rgbled(RGB_GREEN)  
                 
                with open('inventory.json', 'w') as f:
                    json.dump(data, f)  

                print(data)
            else:
                print('unable to determine its UID, try again')
                pycom.rgbled(RGB_RED)             
            
            time.sleep(2)    
            print('Scanning for products')      
        else:   
            pycom.rgbled(RGB_BLUE)
except:
    pycom.heartbeat(False)
    nfc.mfrc630_cmd_reset()
    time.sleep(.5)    
    nfc.mfrc630_cmd_init()    
