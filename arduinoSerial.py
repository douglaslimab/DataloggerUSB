import psycopg2
import serial
import time

arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
temp_pack = []
waiting_time = 1

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data

def arduino_read():
    data_rx = arduino.readline()
    return data_rx[:5]

def insert_temperature(temperature, time):
    # sql code
    sql = """INSERT INTO temperature_logger(temperature, time)
             VALUES(%s, %s) RETURNING temp_id"""

    # db connection
    con = psycopg2.connect(
        host = "localhost",
        database = "temperature",
        user = "postgres",
        password = "Classic-2011"
    )

    temp_id = None

    try:
        # create cursor
        cur = con.cursor()
        # execute sql insert
        cur.execute(sql, (temperature, time,))

        temp_id = cur.fetchone()[0]

        # commit sql code
        con.commit()
        # close cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if con is not None:
            con.close()

    return temp_id


while True:
#    num = input("Enter a number: ") # Taking input from user
#    temp_pack.insert(0, str(value, "utf-8"))
#    if(len(temp_pack) >= 1):
#        sum_up = sum(temp_pack)/len(temp_pack)
#        print(sum_up)
#    print(temp_pack)

    # get data
    start = time.time()
    value = arduino_read()
    time_logger = str(time.localtime().tm_hour) + ':' + str(time.localtime().tm_min) + ':' + str(time.localtime().tm_sec)

    # insert data base
    if(str(value, 'utf-8') != ''):
        # print data
        print(f"Sample nº {insert_temperature(str(value, 'utf-8'), time_logger)}\n{str(value, 'utf-8')} °C at {time_logger}")

#        insert_temperature(str(value, "utf-8"), time_logger)

    end = time.time()
    if(end - start) < waiting_time:
        time.sleep(waiting_time - (end - start))
    else:
        time.sleep(end - start)


#   next steps
#   save data do csv
#   plot data