from Database.Entities.Account import Accounts
from Database.Entities.TransactionTypes import TransactionTypes


class Transaction:
    """static class for holding constants for Transaction table"""
    TABLE_NAME = "transactions"
    COLUMN_TRANSACTION_ID = "transaction_id"
    COLUMN_DATE = "date_of_transaction"
    COLUMN_AMOUNT_OF_TRANSACTION = "amount_of_transaction"
    COLUMN_FROM_ACCOUNT_ID = 'from_account'
    COLUMN_TO_ACCOUNT_ID = "to_account"
    COLUMN_TRANSACTION_TYPE_CODE = "transaction_type_code"
    COLUMN_OTHER_DETAILS = "other_details"

    @classmethod
    def getCreateQuery(cls):
        return (f"CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME}("
                f"{cls.COLUMN_TRANSACTION_ID} INT(10) PRIMARY KEY AUTO_INCREMENT ,"
                f"{cls.COLUMN_DATE} datetime,"
                f"{cls.COLUMN_AMOUNT_OF_TRANSACTION} DECIMAL(11,2),"
                f"{cls.COLUMN_FROM_ACCOUNT_ID} INT(10),"
                f"{cls.COLUMN_TO_ACCOUNT_ID} INT(10),"
                f"{cls.COLUMN_TRANSACTION_TYPE_CODE} INT(10),"
                f"{cls.COLUMN_OTHER_DETAILS} VARCHAR(30),"
                f"FOREIGN KEY({cls.COLUMN_FROM_ACCOUNT_ID}) REFERENCES"
                f" {Accounts.TABLE_NAME}({Accounts.COLUMN_ACCOUNTS_ID}),"
                f"FOREIGN KEY({cls.COLUMN_TO_ACCOUNT_ID}) REFERENCES"
                f" {Accounts.TABLE_NAME}({Accounts.COLUMN_ACCOUNTS_ID}),"
                f"FOREIGN KEY({cls.COLUMN_TRANSACTION_TYPE_CODE}) REFERENCES "
                f"{TransactionTypes.TABLE_NAME}({TransactionTypes.COLUMN_TRANSACTION_TYPES_CODE}));")
