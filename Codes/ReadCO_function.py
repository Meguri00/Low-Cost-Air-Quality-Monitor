import serial
import csv
import datetime

def ReadCO():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    data = ser.readline().decode().strip()
    co_concentration = data.split()[0]
    return float(co_concentration)
    

    