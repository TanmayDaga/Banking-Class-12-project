from MyDbHelper import MyDbHelper
from QueryManager import QueryManger
from Constants import *

if __name__ == "__main__":
    db = MyDbHelper(host="localhost", user="root", password="TanmayDaga")
    qm = QueryManger(db)

    qm.addQuery(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};")

    qm.addQuery(f"USE {DATABASE_NAME}")

    # Creating table account types
    qm.addQuery(f"CREATE TABLE IF NOT EXISTS {TABLE_ACCOUNT_TYPES}("
                f"{COLUMN_ACCOUNT_TYPES_CODE} INT(10) PRIMARY KEY,"
                f"{COLUMN_ACCOUNT_TYPES_DESCRIPTION} VARCHAR(40));")

    qm.addQuery(f"CREATE TABLE IF NOT EXISTS {TABLE_ACCOUNTS}("
                f"{COLUMN_ACCOUNTS_ID} INT(10) PRIMARY KEY,"
                f"{COLUMN_ACCOUNT_HOLDER_NAME} VARCHAR(40) NOT NULL,"
                f"{COLUMN_ACCOUNT_HOLDER_DOB} DATE NOT NULL,"
                f"{COLUMN_ACCOUNT_HOLDER_ADDRESS} VARCHAR(100) NOT NULL,"
                f"{COLUMN_ACCOUNT_OPEN_DATE} DATE DEFAULT (CURDATE()),"
                f"{COLUMN_OTHER_ACCOUNT_DETAILS} VARCHAR(100),"
                f"{COLUMN_ACCOUNT_TYPE} INT(10),"
                f"FOREIGN KEY ({COLUMN_ACCOUNT_TYPE}) REFERENCES {TABLE_ACCOUNT_TYPES}({COLUMN_ACCOUNT_TYPES_CODE}));")


    qm.addQuery(f"CREATE TABLE IF NOT EXISTS {TABLE_TRANSACTION_TYPES}("
                f"{COLUMN_TRANSACTION_TYPES_CODE} INT(10) PRIMARY KEY,"
                f"{COLUMN_ACCOUNT_TYPES_DESCRIPTION} VARCHAR(40));")


    qm.executeAll()
