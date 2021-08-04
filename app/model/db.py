from abc import ABC
import mysql.connector

class DB(ABC):
    conn = mysql.connector.connect(
        host='mysql:3306',
        user='root',
        password='toor',
        database='db',
        port=3306
    )

    @staticmethod
    def connect():
        try:
            cursor = DB.conn.cursor(dictionary=True)
            return cursor
        except mysql.connector.Error as e:
            print(e)
