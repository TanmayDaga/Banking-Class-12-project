from Database.Entities.Users import Users
from Log import Log
from Constants import *

from Database.Entities.Account import Accounts
from Database.Entities.AccountTypes import AccountType
from Database.Entities.TransactionTypes import TransactionTypes
from Database.Entities.Transactions import Transaction
import Database.DummyData as DummyData
from Database.QueryManager import QueryManger
from Database.MyDbHelper import MyDbHelper
from mysql.connector.connection import MySQLCursor


class Repository:
    __instance = None
    __dbHelper = None
    __queryManager = None

    @staticmethod
    def get_instance():
        if Repository.__instance is None:
            Repository.__instance = Repository()
            Log.info(__file__, "Repository instance created")
        return Repository.__instance

    def setDbHelper(self, host, user, password):
        Log.info(__file__, f"{host},{user},{password}")
        if Repository.__dbHelper is None:
            Repository.__dbHelper = MyDbHelper(host=host, user=user, password=password)

        self.__setQueryManager()
        self.__initialiseDb()

    def __setQueryManager(self):
        if Repository.__queryManager is None:
            Repository.__queryManager = QueryManger(self.__dbHelper)
            Log.warn(__file__, "queryManager already set")

    def __initialiseDb(self):
        if self.__queryManager is not None:
            self.__queryManager.addQuery(f"DROP DATABASE {DATABASE_NAME}")
            self.__queryManager.addQuery(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};")

            self.__queryManager.addQuery(f"USE {DATABASE_NAME}")

            # Creating table account types
            self.__queryManager.addQuery(AccountType.getCreateQuery())
            self.__queryManager.addQuery(Accounts.getCreateQuery())

            self.__queryManager.addQuery(TransactionTypes.getCreateQuery())
            self.__queryManager.addQuery(Transaction.getCreateQuery())

            self.__queryManager.addQuery(Users.getCreateQuery())
            self.__queryManager.executeAll()

            DummyData.insertDummyData(self.__queryManager)

    def validator(self, userid: str, password: str) -> (bool, int):
        try:
            cursor = self.__queryManager.execute(
                f'SELECT {Users.COLUMN_ACCOUNT_ID} FROM {Users.TABLE_NAME} WHERE {Users.COLUMN_USERID} = "{userid}" and {Users.COLUMN_PASSWORD} = "{password}"')
            records = cursor.fetchall()

            if len(records) != 0:
                for row in records:
                    return True, row[0]
        except Exception as e:
            Log.error(__file__, str(e))

        return False, None

    def getDataById(self, userId: int) -> MySQLCursor:
        """
        The getDataById function accepts an integer as a parameter and returns the data associated with that account.
        The function is used to retrieve the data of a specific account from the database.

        :param self: Used to Access variables that belongs to the class.
        :param userId:int: ID Of account whose data to be accessed.
        :return: The data of the account holder with the given id.
        """

        try:
            cursor = self.__queryManager.execute(
                f'SELECT {Accounts.COLUMN_ACCOUNT_HOLDER_NAME},{Accounts.COLUMN_ACCOUNT_HOLDER_DOB},'
                f'{Accounts.COLUMN_ACCOUNT_HOLDER_ADDRESS},{Accounts.COLUMN_ACCOUNT_PHONE_NUMBER},{Accounts.COLUMN_ACCOUNT_EMAIL_ID},'
                f'{Accounts.COLUMN_ACCOUNT_BALANCE},{Accounts.COLUMN_ACCOUNT_OPEN_DATE},{Accounts.COLUMN_OTHER_ACCOUNT_DETAILS},{Accounts.COLUMN_ACCOUNT_TYPE} '
                f' FROM {Accounts.TABLE_NAME} WHERE {Accounts.COLUMN_ACCOUNTS_ID} = {userId};')
            return cursor
        except Exception as e:
            Log.error(__file__, str(e))

        return None

    def getDescriptionOfAccountType(self, accountTypeCode) -> str:
        """
        The getDescriptionOfAccountType function accepts an account type code and returns the description of that
        account type.

        :param self: Used to Access variables that belongs to the class.
        :param accountTypeCode: Used to Get the description of an account type.
        :return: The description of the account type.
        """

        try:
            cursor = self.__queryManager.execute(
                f'SELECT {AccountType.COLUMN_ACCOUNT_TYPES_DESCRIPTION} FROM {AccountType.TABLE_NAME} WHERE {AccountType.COLUMN_ACCOUNT_TYPES_CODE} = {accountTypeCode};')
            records: list = cursor.fetchall()
            return records[0][0]

        except Exception as e:
            Log.error(__file__, "Error retriveing account Type:" + str(e))

        return None

    def getOtherUsersForTransactions(self, currUserId: int) -> list:
        """
        The getOtherUsersForTransactions function returns a list of all the other users who have accounts in the database.
        The function takes one argument, currUserId, which is an integer representing the current user's account ID.

        :param self: Used to Access variables that belongs to the class.
        :param currUserId:int: Used to Check if the account holder name is not equal to the current user id.
        :return: A list of all the other users who have accounts in the database.
        """

        try:
            cursor = self.__queryManager.execute(
                f'SELECT {Accounts.COLUMN_ACCOUNT_HOLDER_NAME} FROM {Accounts.TABLE_NAME} WHERE {Accounts.COLUMN_ACCOUNTS_ID} <> {currUserId};'
            )
            records: list = cursor.fetchall()

            resultList: list = list(
                map(lambda x: x[0], records))  # records = [["williamjones",],["otherusername"],....]

            return resultList

        except Exception as e:
            Log.error(__file__, "Error Retriveing other user names " + str(e))

        return None

    def getTransactionTypes(self) -> list:
        """
        The getTransactionTypes function returns a list of all the transaction types in the database.
        The function takes no arguments and returns a list of strings.

        :param self: Used to Access variables that belongs to the class.
        :return: A list of all the transaction types in the database.

        :doc-author: Trelent
        """

        try:
            cursor = self.__queryManager.execute(
                f'SELECT {TransactionTypes.COLUMN_TRANSACTION_TYPES_DESCRIPTION} FROM {TransactionTypes.TABLE_NAME};'
            )
            records: list = cursor.fetchall()

            resultList: list = list(
                map(lambda x: x[0], records))  # records = [["rtgs",],["neft"],....]

            return resultList

        except Exception as e:
            Log.error(__file__, "Error Retriveing other user names " + str(e))

        return None
