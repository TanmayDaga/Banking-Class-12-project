from Database.Entities import Transactions
from Database.Entities.Account import Accounts
from Log import Log

from Database.DummyData import dummyTransactionData


def insertDummyData(repoInstance):
    # --------------------------------------- Into Account Types---------------------------------------
    repoInstance.execute(
        'INSERT INTO account_types(account_types_code,account_types_description) VALUES(1,"Current Account");')
    repoInstance.execute(
        'INSERT INTO account_types(account_types_code,account_types_description) VALUES(2,"Savings Account");')
    repoInstance.execute(
        'INSERT INTO account_types(account_types_code,account_types_description) VALUES(3,"Salary Account");')

    #   ---------------------------------------    Into Accounts    ---------------------------------------
    repoInstance.execute(
        """
       INSERT INTO accounts(account_name,account_holder_dob,account_holder_address,account_holder_phone_no,account_holder_email_id,balance,account_open_date,account_details,account_type) 
VALUES
  ("Indira Goodwin","1940-06-08","Ap #620-7995 Sed Rd.",5424828298,"accumsan.sed@icloud.net",5230376,"2008-09-26 ","null",2),
  ("Seth Grimes","1918-05-16","Ap #912-1068 Pellentesque St.",3900271925,"tortor@outlook.com",7028900,"2006-10-11 ","null",3),
  ("Guinevere Turner","1979-11-15","P.O. Box 985, 9227 Lobortis St.",8827672605,"augue.eu.tellus@aol.com",5547410,"2009-01-17 ","null",2),
  ("Jason Snyder","1946-11-05","329-3350 Nonummy St.",8962140424,"a.magna@yahoo.net",6975482,"1992-09-09 ","null",1),
  ("Cullen Espinoza","1939-04-02","675-6501 Nulla Ave",3985036671,"turpis@hotmail.couk",5240395,"2008-01-16 ","null",1),
  ("Britanni Skinner","1958-10-07","599-2319 Egestas Ave",4291281578,"aliquet@protonmail.org",6750090,"1981-02-08 ","null",2),
  ("Declan Chaney","1981-04-01","Ap #263-4743 Velit. St.",5794843985,"faucibus@google.edu",7341591,"1993-03-12 ","null",1),
  ("Joel Riley","1947-06-25","7683 Eu, Av.",9793868419,"dolor.fusce.feugiat@protonmail.org",7480685,"1976-05-09 ","null",3),
  ("Kenneth Conner","1930-05-25","5024 Aliquet Street",8479646333,"volutpat.nulla@outlook.org",174836,"1996-02-18 ","null",2),
  ("Kennan Sharpe","1965-04-10","290-6369 Semper Ave",4539123437,"duis@protonmail.org",8000123,"2016-09-05 ","null",1);
        """
    )

    repoInstance.execute("""
            INSERT INTO accounts(account_name,account_holder_dob,account_holder_address,account_holder_phone_no,account_holder_email_id,balance,account_open_date,account_details,account_type) 
VALUES
      ("Astra Clemons","1941-07-12","422-4506 Sagittis Rd.",1026304935,"sed@yahoo.org",1545018,"1979-08-31 ","null",3),
      ("Shellie Savage","1951-04-19","7676 Vel Road",7453364132,"pellentesque.ultricies@hotmail.couk",8925482,"2005-03-25 ","null",2),
      ("Armando Robles","1956-12-23","322-975 Aliquam Av.",6892136119,"integer@yahoo.org",1610813,"2016-02-08 ","null",3),
      ("Adria Francis","1948-09-19","873-3027 Conubia Street",4400357255,"eleifend.cras@outlook.org",4783272,"1984-01-19 ","null",2),
      ("Adria Hicks","1960-11-16","Ap #575-5367 Velit. St.",5632248231,"malesuada@outlook.edu",6120418,"1974-05-03 ","null",3),
      ("Quintessa Richmond","1946-08-10","807-8611 Fermentum Rd.",9504390793,"egestas.fusce@protonmail.org",3017467,"2002-05-31 ","null",1),
      ("Keith Barrera","1968-02-23","P.O. Box 673, 5253 Nonummy. St.",3885211570,"sodales.purus@outlook.edu",2508957,"1998-06-28 ","null",2),
      ("Sandra Fuentes","1969-07-04","Ap #569-8892 Phasellus Avenue",4121594027,"leo@yahoo.edu",7667922,"1976-09-28 ","null",2),
      ("Scarlett Vaughn","1943-01-09","Ap #841-473 A Street",2804977872,"erat.volutpat@protonmail.couk",6529579,"1969-08-17 ","null",1),
      ("Carlos Pena","1965-10-25","725-8607 Etiam Street",1011534211,"semper@protonmail.couk",4414468,"1982-04-08 ","null",3);
        """)

    repoInstance.execute("""
        INSERT INTO accounts(account_name,account_holder_dob,account_holder_address,account_holder_phone_no,account_holder_email_id,balance,account_open_date,account_details,account_type) 
VALUES
      ("Neil Adams","1980-07-27","P.O. Box 292, 2078 Nibh Rd.",3365963448,"sed.sapien@google.net",981983,"2022-10-11 ","null",2),
      ("Jasmine Conley","1946-08-11","P.O. Box 263, 7711 Luctus, Street",8875563728,"sodales.purus@icloud.net",8465370,"1968-03-04 ","null",3),
      ("Fritz Pace","1974-08-07","Ap #765-1731 Pellentesque St.",9874812633,"fermentum.arcu@aol.net",67855,"1981-07-30 ","null",1),
      ("Wyoming Ramos","1978-10-05","6884 Pellentesque Av.",7438398682,"fermentum.metus@hotmail.couk",6920183,"2012-07-05 ","null",2),
      ("Ainsley Lane","1974-01-28","P.O. Box 515, 835 Egestas Ave",1299694945,"nec.diam.duis@hotmail.com",526539,"2015-12-17 ","null",3),
      ("Shay Rich","1931-05-20","P.O. Box 637, 6133 Convallis Street",3921793066,"praesent.eu@aol.edu",2935797,"1992-08-21 ","null",1),
      ("Audra Aguirre","1978-01-09","862-6228 Nec Rd.",9393111114,"duis.gravida@protonmail.ca",7905753,"2006-02-04 ","null",2),
      ("Justine Snyder","1965-01-06","P.O. Box 605, 6091 Proin Road",6501353192,"lacus@hotmail.couk",4575290,"2002-09-22 ","null",3),
      ("Nasim Cline","1923-12-16","P.O. Box 598, 7598 Elit, Av.",3956706190,"viverra.donec@icloud.ca",5051395,"2004-03-21 ","null",3),
      ("Troy Cain","1926-12-20","P.O. Box 209, 5086 Augue Street",3485949728,"nunc.ullamcorper@google.edu",7614942,"1973-07-21 ","null",2);
        """)

    repoInstance.execute("""
        INSERT INTO accounts(account_name,account_holder_dob,account_holder_address,account_holder_phone_no,account_holder_email_id,balance,account_open_date,account_details,account_type) 
VALUES
      ("Chase Suarez","1975-07-05","P.O. Box 149, 2247 Venenatis St.",9717199009,"scelerisque.lorem.ipsum@google.edu",3448420,"2004-11-29 ","null",2),
      ("Daquan Owen","1934-08-13","457-3628 Hendrerit. Street",2627814573,"lobortis.ultrices.vivamus@icloud.couk",4330655,"2002-09-27 ","null",3),
      ("Rafael Madden","1918-08-29","684-9067 A, Avenue",6318368853,"sapien.cursus.in@yahoo.com",9642878,"1967-05-15 ","null",1),
      ("Cedric Stafford","1922-04-13","8271 Donec Ave",9778053700,"non.lobortis.quis@aol.net",4751098,"2014-09-20 ","null",2),
      ("Suki Burton","1949-08-25","429-3565 Imperdiet Ave",2051525597,"mauris.sapien@yahoo.couk",9923164,"1968-03-16 ","null",2),
      ("Raphael Brennan","1975-10-12","Ap #679-6164 Urna, Street",1922129234,"dignissim.magna@yahoo.couk",8341497,"1976-09-07 ","null",3),
      ("Maris Briggs","1976-01-26","Ap #986-625 Enim Street",2945948136,"sed.dictum.proin@google.org",5792343,"2010-06-16 ","null",2),
      ("Hoyt Battle","1927-01-22","159-1245 Phasellus Road",1735448007,"in.ornare@aol.ca",6668541,"2007-02-04 ","null",1),
      ("Keegan Espinoza","1966-05-09","Ap #767-3908 Facilisis Avenue",6426295665,"ac.mi@hotmail.edu",9418823,"2015-05-27 ","null",2),
      ("Tad Bowers","1974-06-21","Ap #796-4151 Vitae, St.",4112738091,"convallis@protonmail.ca",321843,"1980-09-02 ","null",2);
        """)

    # --------------------------------------- Into transaction types---------------------------------------
    repoInstance.execute(
        """INSERT INTO transaction_types(transaction_type_code,transaction_types_description) 
        VALUES(1,"NEFT"),(2,"RTGS"),(3,"IMPS"),(4,"UPI"),(5,"AEPS"),(6,"BANKING CARDS"),(7,"CHEQUE");""")

    # --------------------------------------- Dummy data for transactions---------------------------------------
    for i in dummyTransactionData.data:
        startTransaction(repoInstance, int(i["from_account"]), int(i["to_account"]), int(i["amount_of_transaction"]),
                         int(i["transaction_type_code"]), i["date_of_transaction"])

    # --------------------------------------- Dummy Data of users---------------------------------------
    repoInstance.execute("""
        INSERT INTO `Users`(USERID,ACCOUNTID)
  SELECT concat("@",account_name),account_id from accounts;
       """)
    # DUmmy Data passwords of users

    # PASSWORDS LIST
    text = "text"
    data = [{text: "amet"}, {text: "Aeneangrav"}, {text: "Fusce"}, {text: "egestas,"},
            {text: "malesuadafames"}, {text: "Integer"}, {text: "non,da"}, {text: "lectus."},
            {text: "sociis"}, {text: "elementum, dui"}, {text: "luctus vulputate,"}, {text: "ullamcorper"},
            {text: "dictum magna"}, {text: "lorem"}, {text: "velit"}, {text: "Utsemper"}, {text: "semper"},
            {text: "eget,"}, {text: "molestie"}, {text: "vitae odio"}, {text: "CuraePhasellus"},
            {text: "consequatne"}, {text: "amet,"}, {text: "nascetur"}, {text: "Donecnibh"}, {text: "molestie"},
            {text: "eros"}, {text: "neccursus"}, {text: "non lorem"}, {text: "Sed"}, {text: "Donec egestas."},
            {text: "libero."}, {text: "non"}, {text: "ametdiam"}, {text: "Nam"}, {text: "porttitor"},
            {text: "tempor"}, {text: "molestiesodales"}, {text: "dictumaugue"}, {text: "facilisismagna"}]
    cursor = repoInstance.execute("SELECT account_name from accounts;")
    records = cursor.fetchall()
    records = list(map(lambda x: x[0], records))
    for i in range(40):
        repoInstance.execute(
            f"update `Users` set password = '{setpassowrdlengthto16(data[i][text])}' WHERE USERID = '@{records[i]}';")


def setpassowrdlengthto16(password) -> str:
    if (len(password) > 16):
        return password[0:16]
    return password


def startTransaction(repoInstance, fromUserId: int, toUserId, amount, transactionType: int, dateOfTransaction):
    try:

        # Getting current User Bank Balance
        cursorAmount = repoInstance.get_instance().execute(
            f"SELECT {Accounts.COLUMN_ACCOUNT_BALANCE} FROM {Accounts.TABLE_NAME} WHERE {Accounts.COLUMN_ACCOUNTS_ID} = {fromUserId}"
        )

        if cursorAmount.fetchall()[0][0] < amount: raise Exception("Not enough balance")

        # Deducting amount
        repoInstance.get_instance().execute(
            f"UPDATE {Accounts.TABLE_NAME} SET {Accounts.COLUMN_ACCOUNT_BALANCE} = {Accounts.COLUMN_ACCOUNT_BALANCE}-{amount} WHERE {Accounts.COLUMN_ACCOUNTS_ID} = {fromUserId}"
        )

        # Crediting amount
        repoInstance.get_instance().execute(
            f"UPDATE {Accounts.TABLE_NAME} SET {Accounts.COLUMN_ACCOUNT_BALANCE} = {Accounts.COLUMN_ACCOUNT_BALANCE}+{amount} WHERE {Accounts.COLUMN_ACCOUNTS_ID} = {toUserId};"
        )

        # Adding the transaction to transaction table

        repoInstance.get_instance().execute(
            f"INSERT INTO {Transactions.Transaction.TABLE_NAME}({Transactions.Transaction.COLUMN_DATE},{Transactions.Transaction.COLUMN_AMOUNT_OF_TRANSACTION},{Transactions.Transaction.COLUMN_FROM_ACCOUNT_ID},{Transactions.Transaction.COLUMN_TO_ACCOUNT_ID},{Transactions.Transaction.COLUMN_TRANSACTION_TYPE_CODE}) VALUES('{dateOfTransaction}',{amount}"
            f",{fromUserId},{toUserId},{transactionType});"
        )
        Log.info(__file__, "Transaction successful")


    except Exception as e:
        Log.error(__file__, str(e))
