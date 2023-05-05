import smbus
import time
import datetime

adress = 0x68
register =  0x00



bus =  smbus.SMBus(2)

def RTCSetTime():
    #get system time
    Systime=datetime.datetime.now()
    #create list of binary values to pass to registers of rtc
    NowTime = [int("0x"+str(Systime.second),16),
               int(("0x"+str(Systime.minute)),16),
               int("0x"+str(Systime.hour),16),
               0x00,
               int("0x"+str(Systime.day),16),
               int("0x"+str(Systime.month),16),
               int("0x"+str(Systime.year)[-2:],16)];
    #write to rtc registers
    bus.write_i2c_block_data(adress,register,NowTime);
    
def RTCReadTime():
    #read registers
    data= bus.read_i2c_block_data(adress,register);
    #each variuable takes register data reads necsasary bits and converts to base 10
    seconds=int(format(data[0],'#010b')[-4:],2)
    tenseconds=int(format(data[0],'#010b')[-8:-4],2)*10
    minutes=int(format(data[1],'#010b')[-4:],2)
    tenminutes=int(format(data[1],'#010b')[-8:-4],2)*10
    hours=int(format(data[2],'#010b')[-4:],2)
    ampm=int(format(data[2],'#010b')[-6],2)
    tenhours=int(format(data[2],'#010b')[-5],2)*10+20*ampm
    day=int(format(data[4],'#010b')[-4:],2)
    tenday=int(format(data[4],'#010b')[-6:-4],2)*10
    month=int(format(data[5],'#010b')[-4:],2)
    tenmonth=int(format(data[5],'#010b')[-5],2)*10
    year=int(format(data[6],'#010b')[-4:],2)
    tenyear=int(format(data[6],'#010b')[-8:-4],2)*10
    century=int(format(data[5],'#010b')[3],2)*10
    #list of time in order of seconds,minutes,hours,day,month,year
    ctime= [seconds+tenseconds,minutes+tenminutes,hours+tenhours,day+tenday,month+tenmonth,year+tenyear+century+2000]
    return(ctime)

    
