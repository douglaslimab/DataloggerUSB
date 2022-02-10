import serial
#import psycopg2
#import time

device = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)

def read():
    rx = device.readline()
    return rx[:5]

def write(tx_data):
    device.write(bytes(tx_data, 'utf-8'))

while(True):
    try:
        if (device == None):
            device = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)

        data = read()
        write('c')
        if str(data, 'utf-8') != '':
            print(str(data, 'utf-8'))
    except:
        if (device != None):
            device.close()
            device = None
        print('no device connected..')
