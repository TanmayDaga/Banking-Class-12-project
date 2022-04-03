from Database import DummyData
from Database.MyDbHelper import MyDbHelper
from Database.QueryManager import QueryManger
from Constants import *

from Database.Entities.Account import Accounts
from Database.Entities.TypesAccount import AccountType
from Database.Entities.TransactionTypes import TransactionTypes
from Database.Entities.Transactions import Transaction


if __name__ == "__main__":
    db = MyDbHelper(host="localhost", user="root", password="TanmayDaga")
    qm = QueryManger(db)
    
    qm.addQuery(f"DROP DATABASE {DATABASE_NAME}")

    qm.addQuery(f"CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};")

    qm.addQuery(f"USE {DATABASE_NAME}")

    # Creating table account types
    qm.addQuery(AccountType.getCreateQuery())
    qm.addQuery(Accounts.getCreateQuery())

    qm.addQuery(TransactionTypes.getCreateQuery())
    qm.addQuery(Transaction.getCreateQuery())


    qm.executeAll()


    DummyData.insertDummyData(qm)