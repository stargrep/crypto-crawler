from sqlite3 import Connection, connect
from typing import Any


def get_connection(db_name: str) -> Connection:
    try:
        return connect(db_name)  # 'test.db'
    except RuntimeError as e:
        print("I am unable to connect to the database" + str(e))


def read(statement: str, db_name: str) -> []:
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


def write(statement: str, db_name: str, *data: Any) -> None:
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


def write_many(statement: str, db_name: str, data_list: []) -> None:
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
