from Database import DummyData
from Database.Entities.Users import Users
from Log import Log
from Constants import *

from Database.Entities.Account import Accounts
from Database.Entities.AccountTypes import AccountType
from Database.Entities.TransactionTypes import TransactionTypes
from Database.Entities.Transactions import Transaction

from Database.MyDbHelper import MyDbHelper
from mysql.connector.connection import MySQLCursor


class Repository:
    """The purpose of class is to establish connection between ui and database"""
    __instance = None
    __dbHelper = None

    @staticmethod
    def get_instance() -> 'Repository':  # Used string as class doesn't exist at the time of parsing
        """The get_instance method is a static method maintaining and returing only single instance of class
        implementing singleton method
        :param:.
        :return: Repository class Instance.
        """
        if Repository.__instance is None:
            Repository.__instance = Repository()
            Log.info(__file__, "Repository instance created")
        return Repository.__instance

    def setDbHelper(self, host, user, password):

        """
        The setDbHelper function is used to set the database helper object.
        It is called by the constructor of the Repository class, and it takes three parameters: host, user and password.
        The function sets a new instance of DbHelper as an attribute on itself with name __dbHelper.

        :param self: Used to Represent the instance of the object itself.
        :param host: Used to Specify the hostname of the database server.
        :param user: Used to Set the user name for the database connection.
        :param password: Used to Set the password for the database.
        :return:.
        """

        Log.info(__file__, f"{host},{user},{password}")
        if Repository.__dbHelper is None:
            Repository.__dbHelper = MyDbHelper(host=host, user=user, password=password)
        self.__initialiseDb()
        

    def __initialiseDb(self):
        """
        The __initialiseDb function is a private function that is called by the constructor of the Database class.
        It creates a database with name 'banking' if it does not exist and then switches to this database.
        The tables are created in this database, including: account types, accounts, transaction types and transactions.
        :param self: Used to Access variables that belongs to the class.
        :return:.
        """

        if self.__dbHelper is not None:
            # for testing purpose
            self.execute(f"DROP DATABASE {DATABASE_NAME}")
            self.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};")

            self.execute(f"USE {DATABASE_NAME}")

            # Creating table account types
            self.execute(AccountType.getCreateQuery())
            self.execute(Accounts.getCreateQuery())

            self.execute(TransactionTypes.getCreateQuery())
            self.execute(Transaction.getCreateQuery())

            self.execute(Users.getCreateQuery())

            # for testing purpose
            DummyData.insertDummyData(self)

    def execute(self, query: str) -> MySQLCursor:

        """
        The execute function takes a query as an argument and returns the cursor object.
        It then executes the query using the cursor object, and if successful, it will return
        the cursor object. If there is an error executing the query, it will log that error and return none.

        :param self: Used to Access variables that belongs to the class.
        :param query:str: Used to Pass in the sql query that will be executed.
        :return: A cursor.
        """

        cursor = self.__dbHelper.getCursor()

        try:
            cursor.execute(query)
            Log.info(__file__, "Query Successful")

            return cursor
        except Exception as e:
            Log.error(__file__, str(e) + "\n" + query)

        cursor.close()
        return None
