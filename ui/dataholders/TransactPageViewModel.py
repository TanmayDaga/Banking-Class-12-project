from typing import Callable
from Repository import Repository
from Log import Log
from Database.Entities.Account import Accounts

from Database.Entities import Transactions, TransactionTypes


class TransactPageViewModel:
    __instance = None

    @staticmethod
    def get_instance() -> 'TransactPageViewModel':  # Used string as class doesn't exist at the time of parsing
        """
        The get_instance method is a static method maintaining and returning only single instance of class
        implementing singleton method
        :param:.
        :return: UpdateViewModel class Instance.
        """
        if TransactPageViewModel.__instance is None:
            TransactPageViewModel.__instance = TransactPageViewModel()
            Log.info(__file__, "TransactionPageViewModel Created")
        return TransactPageViewModel.__instance

    def getUsers(self, fromUserId, onUpdateUsers: Callable[[list], None]):
        """
        The getUsers function retrieves all the users from the database and returns them to the caller.
        The function takes in a callback function as an argument, which is called when there are new records available.
        :param self: Used to Reference the class instance.
        :param onUpdateUsers:Callable[[list],None]:  Used to Pass the list of users to the gui.
        :return: .
        """
        if fromUserId != 0:
            cursor = None
            try:
                cursor = Repository.get_instance().execute(
                    f"SELECT {Accounts.COLUMN_ACCOUNT_HOLDER_NAME} FROM {Accounts.TABLE_NAME} WHERE {Accounts.COLUMN_ACCOUNTS_ID} <> {fromUserId};")

                records = cursor.fetchall()
                if len(records) != 0:
                    records = list(map(lambda x: x[0], records))
                    onUpdateUsers(records)

            except Exception as e:
                Log.error(__file__, str(e))

    def getTransactionTypes(self, onTransactionTypesFetchCompleted: Callable[[list], None]):
        """
        The getTransactionTypes function returns a list of all the transaction types in the database.
        The function takes no arguments and returns a list of strings.

        :param self: Used to Access variables that belongs to the class.
        :return: A list of all the transaction types in the database.
        """

        try:
            cursor = Repository.get_instance().execute(
                f'SELECT {TransactionTypes.TransactionTypes.COLUMN_TRANSACTION_TYPES_DESCRIPTION} FROM {TransactionTypes.TransactionTypes.TABLE_NAME};'
            )
            records: list = cursor.fetchall()

            resultList: list = list(
                map(lambda x: x[0], records))  # records = [["rtgs",],["neft"],....]

            onTransactionTypesFetchCompleted(resultList)

        except Exception as e:
            Log.error(__file__, "Error Retriveing  transaction types" + str(e))

    def startTransaction(self, fromUserId: int, toName, amount, transactionTypeDescription: str,
                         onTransactionCompleted: Callable[[bool, str], None]):

        """
                It takes a userId, a username, an amount, a transaction type description and a callback function as parameters. It
                then gets the accountId of the user with the given username, gets the current balance of the user with the given
                userId, checks if the current balance is greater than the amount, if it is, it deducts the amount from the user's
                account and credits it to the account of the user with the given username, and finally adds the transaction to the
                transaction table

                :param fromUserId: The id of the user who is sending the money
                :type fromUserId: int
                :param toName: The name of the user to whom the transaction is being made
                :param amount: The amount of money to be transferred
                :param transactionTypeDescription: A string literal
                :type transactionTypeDescription: str
                :param onTransactionCompleted: A callback function that will be called when the transaction is completed
                :type onTransactionCompleted: Callable[[bool, str], None]
                """

        # Getting accountId from usernaame
        try:
            cursor = Repository.get_instance().execute(
                f"SELECT {Accounts.COLUMN_ACCOUNTS_ID} FROM {Accounts.TABLE_NAME} WHERE {Accounts.COLUMN_ACCOUNT_HOLDER_NAME} = '{toName}';"
            )
            records = cursor.fetchall()
            if len(records) != 0:
                toUserId = records[0][0]

                # Getting current User Bank Balance
                cursorAmount = Repository.get_instance().execute(
                    f"SELECT {Accounts.COLUMN_ACCOUNT_BALANCE} FROM {Accounts.TABLE_NAME} WHERE {Accounts.COLUMN_ACCOUNTS_ID} = {fromUserId}"
                )

                if cursorAmount.fetchall()[0][0] < amount: raise NotEnoughBalanceExcepiton()

                # Deducting amount
                Repository.get_instance().execute(
                    f"UPDATE {Accounts.TABLE_NAME} SET {Accounts.COLUMN_ACCOUNT_BALANCE} = {Accounts.COLUMN_ACCOUNT_BALANCE}-{amount} WHERE {Accounts.COLUMN_ACCOUNTS_ID} = {fromUserId}"
                )

                # Crediting amount
                Repository.get_instance().execute(
                    f"UPDATE {Accounts.TABLE_NAME} SET {Accounts.COLUMN_ACCOUNT_BALANCE} = {Accounts.COLUMN_ACCOUNT_BALANCE}+{amount} WHERE {Accounts.COLUMN_ACCOUNTS_ID} = {toUserId};"
                )

                # Adding the transaction to transaction table

                Repository.get_instance().execute(
                    f"INSERT INTO {Transactions.Transaction.TABLE_NAME}({Transactions.Transaction.COLUMN_DATE},{Transactions.Transaction.COLUMN_AMOUNT_OF_TRANSACTION},{Transactions.Transaction.COLUMN_FROM_ACCOUNT_ID},{Transactions.Transaction.COLUMN_TO_ACCOUNT_ID},{Transactions.Transaction.COLUMN_TRANSACTION_TYPE_CODE}) VALUES(CURDATE(),{amount}"
                    f",{fromUserId},{toUserId},{self.__getTransactionTypeCodeFromDescription(transactionTypeDescription)});"
                )

                onTransactionCompleted(True, "Transaction Successful!")

        except TypeError as e:
            Log.error(__file__, str(e))
            onTransactionCompleted(False, "User Doesn't Exists")

        except NotEnoughBalanceExcepiton as e:
            Log.error(__file__, str(e))
            onTransactionCompleted(False, e.getMsg())

    def __getTransactionTypeCodeFromDescription(self, description: str):
        cursor = Repository.get_instance().execute(
            f"SELECT {TransactionTypes.TransactionTypes.COLUMN_TRANSACTION_TYPES_CODE} FROM {TransactionTypes.TransactionTypes.TABLE_NAME} WHERE {TransactionTypes.TransactionTypes.COLUMN_TRANSACTION_TYPES_DESCRIPTION} = '{description}'")
        return cursor.fetchall()[0][0]


class NotEnoughBalanceExcepiton(Exception):
    def __init__(self):
        super(NotEnoughBalanceExcepiton, self).__init__("Not Enough Bank Balance")

    def getMsg(self) -> str:
        return "Not Enough Bank Balance"
