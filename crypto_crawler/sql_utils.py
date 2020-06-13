import sqlite3


def get_connection(db_name: str):
    try:
        return sqlite3.connect(db_name)  # 'test.db'
    except RuntimeError as e:
        print("I am unable to connect to the database" + str(e))


def execute_read(statement, db_name):
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


def execute_write(statement, db_name):
    conn = get_connection(db_name)
    try:
        cursor = conn.cursor()
        cursor.execute(statement)
        conn.commit()
        cursor.close()
    except Exception as error:
        print(error)
    finally:
        conn.close()


def execute_write(statement, db_name, *data):
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


def execute_write_many(statement, db_name, data_list):
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


def create_table_if_not_exist(statement, db_name):
    execute_write(statement, db_name)
    print("table created! - " + statement)


def get_data(statement, db_name):
    return execute_read(statement, db_name)


def insert_many(statement, db_name, data_list):
    execute_write_many(statement, db_name, data_list)
    print("insert - " + statement)
