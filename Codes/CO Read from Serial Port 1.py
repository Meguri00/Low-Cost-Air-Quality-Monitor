import serial
import csv
import datetime

ser = serial.Serial('/dev/ttyACM0', 9600)
with open('/home/tongmu/Desktop/MainProgram/CO_data.csv', 'w', newline='') as file:
    writer =csv.writer(file)
    writer.writerow(['CO Concentration(ppm)'])
    
while True:
    data = ser.readline().decode().strip()
    co_concentration = data.split()[0]
    
    with open('/home/tongmu/Desktop/MainProgram/CO_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([co_concentration])
        print(co_concentration)

