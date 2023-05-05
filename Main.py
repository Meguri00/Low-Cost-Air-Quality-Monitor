import matplotlib.pyplot as plt
import csv
import time
import os
from RTC import*
from PM1 import*
#from PM2 import*
from light import*
from TempHumidPress import*
from ReadCO_function import*
from scd30_i2c import SCD30#CO2 sensor

#DO NOT SET RTC TIME UNLESS CONECTED TO INTERNET AND THE TIME ON THE COMPUTERS CLOCK IS CORRECT!
#setting the rtc time is done by opening the RTC.py file and running it and then calling the RTCSetTime() function
#while the Potato is connected to the internet and the time is correct

scd30 = SCD30()

scd30.set_measurement_interval(60)
scd30.start_periodic_measurement()

time.sleep(2)


#CreatingCSV save data to
if not os.path.exists('/home/tongmu/Desktop/MainProgram/sensor_data.csv'):
    with open('/home/tongmu/Desktop/MainProgram/sensor_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['timestamp','seconds', 'minutes', 'hours', 'day','month','year', 'co2','co','PM1','light','temp in c','pressure','humidity'])
       #PM1-no marking PM2-marked with small dot on the top side on the corner of the metal square bit 

#setup to read every minute
PreviousTime=61
CurrentTime=(RTCReadTime())[1]

#CO2 Measurement Variable
m=0
#Main loop
while True:
    if os.path.exists('/home/tongmu/Desktop/MainProgram/sensor_data.csv'):
        exists_time = time.time() - os.path.getmtime('/home/tongmu/Desktop/MainProgram/sensor_data.csv')
        if exists_time > 7*24*60*60:
            os.remove('/home/tongmu/Desktop/MainProgram/sensor_data.csv')
    
    """  OLD CO2 CODE              
    scd30.read_measurement()
    result = scd30.read_measurement()
    co2 = result[0]
    """
    
    
    if scd30.get_data_ready():
        m = scd30.read_measurement()
        #if m is not None:
            #print(f"CO2: {m[0]:.2f}ppm, temp: {m[1]:.2f}'C, rh:{m[2]:.2f}%")
        time.sleep(1)
    else:
        time.sleep(0.2)

    co2=m[0]
    CurrentTime=(RTCReadTime())[1]
    if CurrentTime!=PreviousTime:
        with open('/home/tongmu/Desktop/MainProgram/sensor_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            ReadingTime=RTCReadTime()
            writer.writerow([time.time(),ReadingTime[0],ReadingTime[1],ReadingTime[2],ReadingTime[3],ReadingTime[4],ReadingTime[5], co2,ReadCO(),PM1Read(),ReadLight(),ReadTempHumidPress()[0],ReadTempHumidPress()[2],ReadTempHumidPress()[3]])
            print([time.time(),ReadingTime[0],ReadingTime[1],ReadingTime[2],ReadingTime[3],ReadingTime[4],ReadingTime[5], co2,ReadCO(),PM1Read(),ReadLight(),ReadTempHumidPress()[0],ReadTempHumidPress()[2],ReadTempHumidPress()[3]])
    PreviousTime=CurrentTime
    
    
    
    
    
    
"""        
    with open('/home/tongmu/Desktop/MainProgram/sensor_data.csv', 'r')as file:
        reader = csv.DictReader(file)
        times = []
        co2_values = []
        for row in reader:
            times.append(float(row['timestamp']))
            co2_values.append(float(row['co2']))"""
            
   
    #line.set_xdata(times)
    #line.set_ydata(co2_values)
    #ax.relim()
    #ax.autoscale_view()
    #plt.draw()
    #plt.pause(1)

#print(co2)



        
#moved down to be out of way                
"""fig, ax = plt.subplots()
times = []
co2_values = []
line, = ax.plot(times, co2_values)
plt.xlabel('Time')
plt.ylabel("CO2(ppm)")
plt.title("CO2 Data from SCD30 Sensor")
"""