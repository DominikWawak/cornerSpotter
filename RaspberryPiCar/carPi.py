#!/usr/bin/python3

from urllib.request import urlopen
import  json
import  time
import serial

WRITE_API_KEY='KG7OEJIPX7TJNDND'

baseURL='https://api.thingspeak.com/update?api_key=%s' % WRITE_API_KEY



def writeData(detected):
    # Sending the data to thingspeak in the query string
    conn = urlopen(baseURL + '&field1=%s' % (detected))
    print(conn.read())
    # Closing the connection
    conn.close()

while True:
    detected=0
    with serial.Serial('/dev/serial0', 115200, timeout=10) as ser:
         message = ser.readline()
    if message:
        detected=1
    writeData(detected)
    time.sleep(20)

