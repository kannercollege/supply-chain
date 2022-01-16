from MFRC630 import MFRC630
from pycoproc_1 import Pycoproc
import time
import pycom
import json

py = Pycoproc(Pycoproc.PYSCAN)
nfc = MFRC630(py)

#RGB_BRIGHTNESS = 0x8
RGB_RED = (0x7f0000)
RGB_GREEN = (0x007f00)
RGB_BLUE = (0X8)

# Make sure heartbeat is disabled before setting RGB LED
pycom.heartbeat(False)

# Initialise the MFRC630 with some settings
nfc.mfrc630_cmd_init()
print('Scanning for videos')
while True:
    # Read out RFID-tag
    atqa = nfc.mfrc630_iso14443a_WUPA_REQA(nfc.MFRC630_ISO14443_CMD_REQA)
    if (atqa != 0):
        # A card has been detected, read UID
        print('A video has been detected, reading its UID ...')
        uid = bytearray(10)
        uid_len = nfc.mfrc630_iso14443a_select(uid)        
        print(str(nfc.format_block(uid, uid_len)))
        pycom.rgbled(RGB_GREEN)

        time.sleep(2)

        print("")
        print('Scanning for videos')
        
    else:
        pycom.rgbled(RGB_BLUE)
    nfc.mfrc630_cmd_reset()
    time.sleep(.5)    
    nfc.mfrc630_cmd_init()
    