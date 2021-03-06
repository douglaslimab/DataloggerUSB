import serial
from tkinter import *
import psycopg2
import time
import csv
import matplotlib.pyplot as plt
from tk_test import App


screen = Tk()
screen.title("Datalogger")
screen.geometry("400x100")
screen.resizable(False, False)

display = Frame(screen)
display.pack(expand=0, pady=10)

control = Frame(screen)
control.pack(expand=0)


device = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)
sample = {}


def read():
    rx = device.readline()
    return rx[:5]


def write(tx_data):
    device.write(bytes(tx_data, 'utf-8'))


def save():
    w = csv.writer(open("output.csv", "w"))
    for key, value in sample.items():
        w.writerow([key, value])


def generate_graphic():
    time = list(sample.keys())
    temp = list(sample.values())

    plt.plot(time, temp)
    plt.show()


def disconnect():
    global device

    screen.after_cancel(timer)
    device.close()
    device = None
    label.configure(text='')
    label_time.configure(text='')
    check.configure(text=str('Disconnected..'), fg="#FF0000")


def connect():
    global timer
    global device

    try:
        if device == None:
            device = serial.Serial(port='COM4', baudrate=115200, timeout=0.1)

        data = read()
        write('c')
        check.configure(text=str('Connected..'), fg="#00FF00")

        time_logger = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(
            time.localtime().tm_sec)

        if str(data, 'utf-8') != '':
            label.configure(text=str(data, 'utf-8'))
            label_time.configure(text=time_logger)
            print(db_insert(str(data, 'utf-8'), time_logger))
            sample[time_logger] = str(data, 'utf-8')
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
        host="localhost",
        database="temperature",
        user="postgres",
        password="cortsolo2006"
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


label = Label(display, text='', width=20, background="#333333", fg="#00FF00")
label.grid(column=0, row=0)

label_time = Label(display, text='', width=20, background="#333333", fg="#00FF00")
label_time.grid(column=1, row=0)

con_btn = Button(control, text="Connect", command=connect)
con_btn.grid(column=0, row=0)

dis_btn = Button(control, text="Disconnect", command=disconnect)
dis_btn.grid(column=1, row=0)

sav_btn = Button(control, text="Save", command=save)
sav_btn.grid(column=2, row=0)

graph_btn = Button(control, text="Graphic", command=generate_graphic)
graph_btn.grid(column=3, row=0)

check = Label(control, text='Disconnected..', width=20, fg="#FF0000")
check.grid(column=0, row=1, columnspan=2)

screen.mainloop()
