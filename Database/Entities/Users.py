from Database.Entities.Account import Accounts


class Users:
    TABLE_NAME = "Users"
    COLUMN_USERID = "USERID"
    COLUMN_PASSWORD = "PASSWORD"
    COLUMN_ACCOUNT_ID = "ACCOUNTID"

    @classmethod
    def getCreateQuery(cls) -> str:
        return f"""CREATE TABLE {cls.TABLE_NAME}({cls.COLUMN_USERID} VARCHAR(30) UNIQUE,{cls.COLUMN_PASSWORD} VARCHAR(
        16) NOT NULL, {cls.COLUMN_ACCOUNT_ID} int(10) PRIMARY KEY,FOREIGN KEY({cls.COLUMN_ACCOUNT_ID}) REFERENCES {Accounts.TABLE_NAME}( 
        {Accounts.COLUMN_ACCOUNTS_ID}));"""
