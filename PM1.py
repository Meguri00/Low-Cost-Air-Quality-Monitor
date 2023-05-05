import serial
import time
from time import sleep


ser=serial.Serial('/dev/ttyUSB0',9600)


#print(data_left.to_bytes(2,'little'))
def PM1Read():
    data=ser.read(10)
    return((data[3]*256+data[4])/10)
