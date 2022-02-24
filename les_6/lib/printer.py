from machine import UART
def print_on_receipt(order):
    # alleen RX gebruiken en aansluiten op P19 (reverse) TX en RX
    uart = UART(1, baudrate=19200, bits=8, parity=None, pins=('P19', 'P15'), timeout_chars =10 , stop=1)

    uart.write('''
********************************
bestelling: 
{}
********************************




'''.format(order).encode('utf-8'))    


