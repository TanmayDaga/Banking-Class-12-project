import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection
from Log import Log


class MyDbHelper:
    __myDb = None
    __cursor = None

    def __init__(self, host="localhost", user="", password="") -> MySQLConnection:

        try:
            self.__myDb = mysql.connector.connect(host=host, user=user, password=password)
            Log.info(__file__, "Connection Established Successfully")
            self.__myDb.autocommit = True

        except Exception as e:
            Log.error(__file__, e)

        __cursor = self.__myDb.cursor()


    def getDb(self):
        return self.__myDb

    def getCursor(self) -> MySQLCursor:
        return self.__myDb.cursor()


    def closeDatabase(self):
        self.__myDb.close()
