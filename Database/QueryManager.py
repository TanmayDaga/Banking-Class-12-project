from Log import Log
import Database.MyDbHelper as MyDbHelper


class QueryManger:
    __queries: list = []
    __myDb: MyDbHelper

    def __init__(self, dbHelper: MyDbHelper):
        self.__myDb = dbHelper


    def addQuery(self, query: str):
        self.__queries.append(query)

    def getQueries(self):
        return self.__queries.copy()

    def execute(self, query: str):
        cursor = self.__myDb.getCursor()
        try:
            cursor.execute(query)
            Log.info(__file__, "Query Successful")
        except Exception as e:
            Log.error(__file__, str(e) + "\n" + query)
        finally:
            cursor.close()

    def executeAll(self):
        for i in self.__queries:
            self.execute(i)
