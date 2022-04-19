import matplotlib.pyplot

from Log import Log
from Database.Entities.Account import Accounts
from Repository import Repository
from typing import Callable
from Database.Entities.AccountTypes import AccountType
from Database.Entities.Transactions import Transaction


class UserInterFaceModel:
    # SOME CONSTANTS for accessing data from dictionary
    KEY_USER_NAME = "username"
    KEY_USER_DOB = "dob"
    KEY_USER_ADDRESS = "address"
    KEY_PHONE_NUMBER = "phone"
    KEY_EMAIL_ID = "emailId"
    KEY_BALANCE_AMOUNT = "balanceAmount"
    KEY_ACCOUNT_OPEN_DATE = "accountOpenDate"
    KEY_ACCOUNT_OTHER_DETAILS = "otherdetails"
    KEY_ACCOUNT_TYPE = "accountType"

    __instance = None
    __curUserId: int = None
    __data: dict = {}

    __onDataChangedFunctions = []  # stores the ui functions which needs to be called

    @staticmethod
    def get_instance() -> 'UserInterFaceModel':  # Used string as class doesn't exist at the time of parsing
        """The get_instance method is a static method maintaining and returning only single instance of class
        implementing singleton method
        :param:.
        :return: UserInterFaceModel class Instance.
        """
        if UserInterFaceModel.__instance is None:
            UserInterFaceModel.__instance = UserInterFaceModel()
            Log.info(__file__, "UserInterfaceViewModel created")
        return UserInterFaceModel.__instance

    def getData(self, userId, onFetchDataCompletion: Callable[[dict], None]) -> None:
        """
        It fetches data from the database and stores it in a dictionary

        :param userId: The user id of the user whose data is to be fetched
        :param onFetchDataCompletion: To be Called when data fetching is completed

        """

        cursor = None
        try:
            cursor = Repository.get_instance().execute(
                f'SELECT {Accounts.COLUMN_ACCOUNT_HOLDER_NAME},{Accounts.COLUMN_ACCOUNT_HOLDER_DOB},'
                f'{Accounts.COLUMN_ACCOUNT_HOLDER_ADDRESS},{Accounts.COLUMN_ACCOUNT_PHONE_NUMBER},{Accounts.COLUMN_ACCOUNT_EMAIL_ID},'
                f'{Accounts.COLUMN_ACCOUNT_BALANCE},{Accounts.COLUMN_ACCOUNT_OPEN_DATE},{Accounts.COLUMN_OTHER_ACCOUNT_DETAILS},{Accounts.COLUMN_ACCOUNT_TYPE} '
                f' FROM {Accounts.TABLE_NAME} WHERE {Accounts.COLUMN_ACCOUNTS_ID} = {userId};')

        except Exception as e:
            Log.error(__file__, str(e))

        if cursor is not None:  # i.e. no error occurred
            records = cursor.fetchone()

            # not using update as to reset data
            self.__data = {UserInterFaceModel.KEY_USER_NAME: records[0],
                           UserInterFaceModel.KEY_USER_DOB: records[1],
                           UserInterFaceModel.KEY_USER_ADDRESS: records[2],
                           UserInterFaceModel.KEY_PHONE_NUMBER: records[3],
                           UserInterFaceModel.KEY_EMAIL_ID: records[4],
                           UserInterFaceModel.KEY_BALANCE_AMOUNT: records[5],
                           UserInterFaceModel.KEY_ACCOUNT_OPEN_DATE: records[6],
                           UserInterFaceModel.KEY_ACCOUNT_OTHER_DETAILS: records[7],
                           UserInterFaceModel.KEY_ACCOUNT_TYPE: self.__getAccountType(records[8])}

        onFetchDataCompletion(self.__data)

    def __getAccountType(self, accountTypeID) -> str:
        """
        The __getAccountType function gets the account type from account type code.
        :param self: Used to Access the attributes and methods of the class in python.
        :param accountTypeID:The Code of the Account Type.
        :return Account Description:.
        """

        cursor = None
        try:
            cursor = Repository.get_instance().execute(
                f"SELECT {AccountType.COLUMN_ACCOUNT_TYPES_DESCRIPTION} FROM  {AccountType.TABLE_NAME} WHERE {AccountType.COLUMN_ACCOUNT_TYPES_CODE} = {accountTypeID}")

        except Exception as e:
            Log.error(__file__, str(e))

        if cursor is not None:
            records = cursor.fetchone()
            return records[0]

    def plotGraph(self, userAccountId, curBalance):
        cursor = Repository.get_instance().execute(f"""
            SELECT {Transaction.COLUMN_AMOUNT_OF_TRANSACTION},{Transaction.COLUMN_FROM_ACCOUNT_ID},{Transaction.COLUMN_TO_ACCOUNT_ID},{Transaction.COLUMN_DATE}
             FROM {Transaction.TABLE_NAME} WHERE {Transaction.COLUMN_FROM_ACCOUNT_ID} = {userAccountId} OR {Transaction.COLUMN_TO_ACCOUNT_ID} = {userAccountId} ORDER BY {Transaction.COLUMN_DATE}
        """)

        records = cursor.fetchall()

        # now records = list of tuples (amount,date_of_transaction)
        records = list(map(lambda x: self.__checkifamountDeducted(x, userAccountId), records))
        amountToBeDeducted = sum(map(lambda x: x[0], records))
        initialBalance = float(curBalance) - amountToBeDeducted  # curbalance is in decimal.decimal datatype
        (x, y) = self.__getAmountToShowList(initialBalance, records)
        fig, ax = matplotlib.pyplot.subplots()
        ax.plot(x, y)

        ax.ticklabel_format(style='plain',axis='y')  # Prevent scientific notaiton
        matplotlib.pyplot.show()

    def __checkifamountDeducted(self, elementx, curUserid) -> tuple:
        """

        :param elementx: object with amount of transaction ,from user id ,touser id
        :param curUserid:current user id
        :return: if amount deducted then false else true
        """
        if curUserid == elementx[1]:
            return (-float(elementx[0]), elementx[3])
        else:
            return (float(elementx[0]), elementx[3])

    def __getAmountToShowList(self, initalBalance, transactionsList):
        curBalance = initalBalance
        finalListY = []
        finalListX = []

        for i in transactionsList:
            curBalance += i[0]
            finalListY.append(curBalance)
            finalListX.append(i[1])

        return finalListX, finalListY
