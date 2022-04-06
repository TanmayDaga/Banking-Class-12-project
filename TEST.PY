from Database.MyDbHelper import MyDbHelper
from Database.Entities.Users import Users
from Log import Log

obj = MyDbHelper(host="localhost", user="root", password="TanmayDaga")
myCur = obj.getCursor()
myCur.execute("use banking")
myCur.execute(
    f'SELECT * FROM {Users.TABLE_NAME} WHERE {Users.COLUMN_USERID} = "@WILLIAMJONES" ')
myCur.fetchall()

Log.info(__file__, f"{myCur.rowcount}")
