import Database.QueryManager as QueryManager


def insertDummyData(qm: QueryManager):
    # Into Account Types
    qm.execute('INSERT INTO account_types(account_types_code,account_types_description) VALUES(1,"Current Account");')
    qm.execute('INSERT INTO account_types(account_types_code,account_types_description) VALUES(2,"Savings Account");')
    qm.execute('INSERT INTO account_types(account_types_code,account_types_description) VALUES(3,"Salary Account");')

    #       Into Accounts
    qm.execute("""INSERT INTO accounts(account_name,account_holder_dob,account_holder_address,balance,account_open_date,account_details,account_type,account_holder_phone_no) 
VALUES("William Jones","1987.06.07","Brown Street,London",78930.23,"1999.08.07","",1,7894320123),
("Charles Green","1988.07.09","Green Avene, NYC",9473.24,"2000.07.06","",2,1839208312),
("Tanmay Daga","1986.05.04","Parvat Patia, Surat",28340.3,"2004.03.02","",1,7389203215),
("Vivek Maheshwari","2000.05.03","vesu",987902.22,"2019.02.01","",2,1893023412);""")

    qm.execute("""INSERT INTO accounts(account_name,account_holder_dob,account_holder_address,balance,account_open_date,
    account_details,account_type,account_holder_phone_no)
VALUES("Vishesh Jain","1978.07.11","Bhatar surat",920238.2,"1988.04.02","",3,7839212352);""")

    qm.execute(
        """INSERT INTO transaction_types(transaction_type_code,transaction_types_description) 
        VALUES(1,"NEFT"),(2,"RTGS"),(3,"IMPS"),(4,"UPI"),(5,"AEPS"),(6,"BANKING CARDS"),(7,"CHEQUE");""")

    qm.execute("""INSERT INTO transactions(date_of_transaction,amount_of_transaction,from_account,to_account,transaction_type_code)
VALUES(CURDATE(),32322,2,1,2),
(CURDATE(),242234,3,2,5),
(CURDATE(),242122,5,2,1),
(CURDATE(),12322,4,3,2);""")

    # Dummy Data of users
    qm.execute("""INSERT INTO `USERS` VALUES("@WILLIAMJONES","ABCDEFGHI",1);""")
    qm.execute("""INSERT INTO `USERS` VALUES("@CHARLESGREEN","HELLOWORLD",2);""")
    qm.execute("""INSERT INTO `USERS` VALUES("@TANMAYDAGA","JLSADKJ",3),("@VIVEKMAHESHWARI","SADJFJLK",4);""")
    qm.execute("""INSERT INTO `USERS` VALUES(@"VISHESHJAIN","SFLAKJ",5);""")
