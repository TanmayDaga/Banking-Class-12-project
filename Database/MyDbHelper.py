import mysql.connector
from mysql.connector.cursor import MySQLCursor
from mysql.connector.connection import MySQLConnection
from Log import Log


class MyDbHelper:
    """Helper class for establishing connections with database"""

    __myDb = None
    __cursor = None

    def __init__(self, host="localhost", user="", password=""):

        try:
            self.__myDb = mysql.connector.connect(host=host, user=user, password=password)
            Log.info(__file__, "Connection Established Successfully")
            self.__myDb.autocommit = True  # Data is inserted automatically without using db.commit() method

        except Exception as e:
            Log.error(__file__, e)

        __cursor = self.__myDb.cursor()

    def getDb(self) -> MySQLConnection:
        """
        The getDb function returns a MySQLConnection object.
        :param self: Used to Access the attributes and methods of the class in python.
        :return: The database connection object.
        """

        return self.__myDb

    def getCursor(self) -> MySQLCursor:
        """
        The getCursor function returns a cursor object that can be used to execute queries.
        :param self: Used to Access the attributes and methods in the parent class.
        :return: A cursor object, which is used to manage the context of a fetch operation.
        """

        return self.__myDb.cursor()

    def closeDatabase(self) -> None:
        """
        The closeDatabase function closes the database connection.
        :param self: Used to Refer to the object itself.
        :return: .
        """

        self.__myDb.close()
