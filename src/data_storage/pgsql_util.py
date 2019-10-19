import psycopg2

def database(db_command_func, *data):
    try:
        conn = psycopg2.connect(dbname='mikedb', user='', host='104.198.59.118', password='')
        print("connection success")
    except:
        print("I am unable to connect to the database")

    result = 0
    if not data:
        result = db_command_func(conn.cursor())
    else:
        result = db_command_func(conn.cursor(), *data)

    conn.commit()
    conn.close()

    return result