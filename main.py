import serial
from tkinter import *

# import psycopg2
# import time

screen = Tk()
screen.title = "Datalogger"
screen.geometry("400x400")

device = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)


def read():
    rx = device.readline()
    return rx[:5]

def write(tx_data):
    device.write(bytes(tx_data, 'utf-8'))

def disconnect():
    global device

    screen.after_cancel(timer)
    device.close()
    device = None
    label.configure(text='')

def connect():
    global timer
    global device

    try:
        if device == None:
            device = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)

        data = read()
        write('c')
        if str(data, 'utf-8') != '':
            label.configure(text=str(data, 'utf-8'))
    except:
        if device != None:
            device.close()
            device = None
        print('no device connected..')

    timer = screen.after(1000, connect)


label = Label(screen, text='')
label.pack()

con_btn = Button(screen, text="Connect", command=connect)
con_btn.pack()

dis_btn = Button(screen, text="Disconnect", command=disconnect)
dis_btn.pack()

screen.mainloop()