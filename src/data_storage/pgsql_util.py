import psycopg2

from src.common.app_constant import PG_DATABASE, PG_USER, PG_HOST, PG_PWD


def get_connection():
    try:
        return psycopg2.connect(dbname=PG_DATABASE, user=PG_USER, host=PG_HOST, password=PG_PWD)
    except RuntimeError as e:
        print("I am unable to connect to the database" + str(e))


def execute_read(statement):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(statement)
        results = cursor.fetchall()
        cursor.close()
        return results
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


def execute_write(statement):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(statement)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


def execute_write(statement, *data):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.execute(statement, data)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


def execute_write_many(statement, data_list):
    conn = get_connection()
    try:
        cursor = conn.cursor()
        cursor.executemany(statement, data_list)
        conn.commit()
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        conn.close()


def create_table_if_not_exist(statement):
    execute_write(statement)
    print("table created! - " + statement)


def get_data(statement):
    return execute_read(statement)


def insert_many(statement, data_list):
    """
    insert many record to data bases

    :param statement: insert statement
    :param data_list: a list of tuple for insertion
    :return: void
    """
    execute_write_many(statement, data_list)
    print("insert - " + statement)
