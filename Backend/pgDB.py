import psycopg2

# sql query
sql = """INSERT INTO temperature_logger(temperature, time)
         VALUES(%s, %s) RETURNING temp_id"""

sql_create_table = """CREATE TABLE test(
                        id SERIAL PRIMARY KEY NOT NULL, 
                        title VARCHAR(50) NOT NULL)"""

sql_insert_table = """INSERT INTO test (title)
                        VALUES(%s) RETURNING id"""

sql_select_table = """SELECT * FROM test"""

# db connection
con = psycopg2.connect(
    host="localhost",
    database="data_logger",
    user="postgres",
    password="cortsolo2006"
)

try:
    # create cursor
    cur = con.cursor()

    # execute sql query
    cur.execute(sql_insert_table, ("douglas",))

    # commit sql code
    con.commit()

    # close cursor
    cur.close()

    print("Data inserted..")
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if con is not None:
        con.close()