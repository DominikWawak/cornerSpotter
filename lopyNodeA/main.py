
# # Please pick the region that matches where you are using the device



from machine import UART
import pycom
import time
from network import LoRa
import socket
import binascii
import struct

pycom.heartbeat(False) # turn off heartbeat

uart1 = UART(1, 9600, bits=8, parity=None, stop=1)
uart1.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=2, pins=("P3", "P4"))
uart1.write("Connected...")

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0


while True:
    
    
   
    if uart1.any():
        data = uart1.read()
        pycom.rgbled(0xFF0000) # set LED to RED on if data received
        if data == b'person':
            pycom.rgbled(0x00FF00) # set LED to GREEN if data is b'send'
            s.send('person')
            print('Ping {}'.format(i) + "person")
            i= i+1
        
        if data == b'car':
            pycom.rgbled(0x0000FF) 
            s.send('car')
            print('Ping {}'.format(i) + "car")
            i= i+1
            
            
        time.sleep(1)
        pycom.rgbled(0x000000)
    time.sleep(0.25)