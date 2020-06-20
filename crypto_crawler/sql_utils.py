import sqlite3


def get_connection(db_name: str):
    try:
        return sqlite3.connect(db_name)  # 'test.db'
    except RuntimeError as e:
        print("I am unable to connect to the database" + str(e))


def read(statement, db_name):
    conn = get_connection(db_name)
    try:
        cursor = conn.cursor()
        cursor.execute(statement)
        results = cursor.fetchall()
        cursor.close()
        return results
    except Exception as error:
        print(error)
    finally:
        conn.close()


def write(statement, db_name, *data):
    conn = get_connection(db_name)
    try:
        cursor = conn.cursor()
        cursor.execute(statement, data)
        conn.commit()
        cursor.close()
    except Exception as error:
        print(error)
    finally:
        conn.close()


def write_many(statement, db_name, data_list):
    conn = get_connection(db_name)
    try:
        cursor = conn.cursor()
        cursor.executemany(statement, data_list)
        conn.commit()
        cursor.close()
    except Exception as error:
        print(error)
    finally:
        conn.close()
