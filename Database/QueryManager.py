from mysql.connector.cursor import MySQLCursor
from Log import Log
import Database.MyDbHelper as MyDbHelper


class QueryManger:
    __queries: list = []
    __myDb: MyDbHelper
    __cursor: MySQLCursor

    def __init__(self, dbHelper: MyDbHelper):
        self.__myDb = dbHelper



    def getCursor(self) -> MySQLCursor:
        return self.__myDb.getCursor()

    def addQuery(self, query: str):
        self.__queries.append(query)

    def getQueries(self):
        return self.__queries.copy()

    def execute(self, query: str) -> MySQLCursor:
        cursor = self.getCursor()

        try:
            cursor.execute(query)
            Log.info(__file__, "Query Successful")

            return cursor
        except Exception as e:
            Log.error(__file__, str(e) + "\n" + query)


        cursor.close()
        return None

    def executeAll(self):
        for i in self.__queries:
            self.execute(i)
