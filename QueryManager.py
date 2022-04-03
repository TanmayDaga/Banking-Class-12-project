import MyDbHelper


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
        self.__myDb.getCursor().execute(query)



    def executeAll(self):
        for i in self.__queries:
            self.execute(i)
