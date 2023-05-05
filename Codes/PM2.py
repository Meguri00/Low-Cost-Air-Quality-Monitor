import serial
import time
from time import sleep


ser=serial.Serial('/dev/ttyUSB1',9600)


#print(data_left.to_bytes(2,'little'))
def PM2Read():
    data=ser.read(10)
    return((data[3]*256+data[4])/10)