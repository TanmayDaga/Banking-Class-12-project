from Database.Entities.AccountTypes import AccountType


class Accounts:
    """static class for holding constants for Accounts table"""

    TABLE_NAME = "accounts"
    COLUMN_ACCOUNTS_ID = "account_id"
    COLUMN_ACCOUNT_HOLDER_NAME = "account_name"
    COLUMN_ACCOUNT_HOLDER_DOB = "account_holder_dob"
    COLUMN_ACCOUNT_HOLDER_ADDRESS = "account_holder_address"
    COLUMN_ACCOUNT_PHONE_NUMBER = "account_holder_phone_no"
    COLUMN_ACCOUNT_EMAIL_ID = "account_holder_email_id"
    COLUMN_ACCOUNT_BALANCE = "balance"
    COLUMN_ACCOUNT_OPEN_DATE = "account_open_date"
    COLUMN_OTHER_ACCOUNT_DETAILS = "account_details"
    COLUMN_ACCOUNT_TYPE = "account_type"

    @classmethod
    def getCreateQuery(cls) -> str:
        return (f"CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME}("
                f"{cls.COLUMN_ACCOUNTS_ID} INT(10) PRIMARY KEY AUTO_INCREMENT ,"
                f"{cls.COLUMN_ACCOUNT_HOLDER_NAME} VARCHAR(40) NOT NULL,"
                f"{cls.COLUMN_ACCOUNT_HOLDER_DOB} DATE NOT NULL,"
                f"{cls.COLUMN_ACCOUNT_HOLDER_ADDRESS} VARCHAR(100) NOT NULL,"
                f"{cls.COLUMN_ACCOUNT_PHONE_NUMBER} DECIMAL(10,0) NOT NULL,"
                f"{cls.COLUMN_ACCOUNT_EMAIL_ID} VARCHAR(80),"
                f"{cls.COLUMN_ACCOUNT_BALANCE} DECIMAL(11,2) NOT NULL,"
                f"{cls.COLUMN_ACCOUNT_OPEN_DATE} DATE DEFAULT (CURDATE()),"
                f"{cls.COLUMN_OTHER_ACCOUNT_DETAILS} VARCHAR(100),"
                f"{cls.COLUMN_ACCOUNT_TYPE} INT(10),"
                f"FOREIGN KEY ({cls.COLUMN_ACCOUNT_TYPE}) "
                f"REFERENCES {AccountType.TABLE_NAME}({AccountType.COLUMN_ACCOUNT_TYPES_CODE}),"
                f"CHECK({cls.COLUMN_ACCOUNT_HOLDER_DOB}+18<={cls.COLUMN_ACCOUNT_OPEN_DATE}));")
