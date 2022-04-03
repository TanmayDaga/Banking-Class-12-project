import mysql.connector


class MyDbHelper:
    __myDb = None
    __cursor = None

    def __init__(self, host="localhost", user="", password=""):

        try:
            self.__myDb = mysql.connector.connect(host=host, user=user, password=password)
        except:
            print("Cannot Instantiate Connector.Please enter valid User Name or Password or Host")

        __cursor = self.__myDb.cursor()


    def getDb(self):
        return self.__myDb

    def getCursor(self):
        return self.__myDb.cursor()

