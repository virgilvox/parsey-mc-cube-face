import os
import serial

ser = serial.Serial('/dev/tty.usbserial-DN05Z2JS', 115200)  # open serial port
print(ser.name)         # check which port was really used
ser.write('MFU\r\n')     # write a string
s = ser.read(512)
print(s)

os.putenv('NEWOTP',s)
os.system('bash')

ser.close()
