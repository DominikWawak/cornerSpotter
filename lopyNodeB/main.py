from network import LoRa
from machine import UART
import socket
import time
import pycom

uart1 = UART(1, 9600, bits=8, parity=None, stop=1)
uart1.init(baudrate=9600, bits=8, parity=None, stop=1, timeout_chars=2, pins=("P3", "P4"))
uart1.write("Connected...")

# Please pick the region that matches where you are using the device
pycom.heartbeat(False) # turn off heartbeat
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)

while True:
    data = s.recv(64)
    print(data)
    if data == b'data':
        
        uart1.write(b'detec')
        pycom.rgbled(0xFF0000) # set LED to 
        s.send('Pong')
        print('Pong ')
        

    # if s.recv(64) == b'data':
    #     pycom.rgbled(0x0000FF) # set LED 
    #     s.send('Pong')
    #     print('Pong {}'.format(i))
    #     i = i+1
    time.sleep(0.5)

