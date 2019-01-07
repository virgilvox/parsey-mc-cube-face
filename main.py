import os
import sys
import serial

port=sys.argv[1]
if port is 'n':
        port = '/dev/tty.usbserial-DN05Z2JS'
print(port)

ser = serial.Serial(port, 115200)  # open serial port
print(ser.name)         # check which port was really used
ser.write('MFU\r\n')     # write a string
s = ser.read(512)
print(s)
ser.write('RF 0\r\n')

os.putenv('NEWOTP',s)
os.system('bash')

ser.close()
