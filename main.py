import serial
from tkinter import *
import psycopg2
import time

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
    label_time.configure(text='')
    check.configure(text=str('Disconnected..'))

def connect():
    global timer
    global device

    try:
        if device == None:
            device = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)

        data = read()
        write('c')
        check.configure(text=str('Connected..'))

        time_logger = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec)

        if str(data, 'utf-8') != '':
            label.configure(text=str(data, 'utf-8'))
            label_time.configure(text=time_logger)
            print(db_insert(str(data, 'utf-8'), time_logger))
            print(f"{str(data, 'utf-8')} | {time_logger}")
    except:
        if device != None:
            device.close()
            device = None
        print('no device connected..')

    timer = screen.after(1000, connect)

def db_insert(temperature, time):
    sql = """INSERT INTO temperature_logger(temperature, time)
             VALUES(%s, %s) RETURNING temp_id"""

    conn = psycopg2.connect(
        host = "localhost",
        database = "temperature",
        user = "postgres",
        password = "cortsolo2006"
    )

    temp_id = None

    try:
        cur = conn.cursor()
        cur.execute(sql, (temperature, time,))

        temp_id = cur.fetchone()[0]

        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return temp_id

def db_read(table, columnA, columnB, n_rows):
    row = {}
    return row

label = Label(screen, text='')
label.pack()

label_time = Label(screen, text='')
label_time.pack()

con_btn = Button(screen, text="Connect", command=connect)
con_btn.pack()

dis_btn = Button(screen, text="Disconnect", command=disconnect)
dis_btn.pack()

check = Label(screen, text='Disconnected..')
check.pack()

screen.mainloop()