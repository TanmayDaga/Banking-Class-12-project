from Log import Log
from typing import Callable
from Repository import Repository
from Database.Entities.Users import Users



class LoginWindowViewModel:
    __instance = None
    __onUserValidatedFunctions = []

    @staticmethod
    def get_instance() -> 'LoginWindowViewModel':  # Used string as class doesn't exist at the time of parsing
        """The get_instance method is a static method maintaining and returning only single instance of class
        implementing singleton method
        :param:.
        :return: UserInterFaceModel class Instance.
        """
        if LoginWindowViewModel.__instance is None:
            LoginWindowViewModel.__instance = LoginWindowViewModel()
            Log.info(__file__, "Login View Model Created")
        return LoginWindowViewModel.__instance

    def addValidateUserObserver(self, fxn: Callable[[int], None]):
        """
        The addValidateUserObserver is used to add observers to userId.
        :param self:Used to access member variables.
        :param fxn:Called when user is validated. The int parameter is for userid
        """
        self.__onUserValidatedFunctions.append(fxn)

    def validateUser(self, username: str, password: str, onValidated: Callable[[bool], None]):

        """
        The validateUser function takes in a username and password as parameters. It then queries the database for that user's information,
        and if it finds it, returns True to onValidated. If not, False is returned.

        :param self: Used to Access the attributes and methods of the class in python.
        :param username:str: Used to Store the username of the user that is trying to login.
        :param password:str: Used to Check if the password entered by the user is correct.
        :param onValidated:Callable[[bool],None]: Used to Pass the result of the validation to the caller.
        :return:.

        :doc-author: Trelent
        """

        cursor = None
        try:
            cursor = Repository.get_instance().execute(
                f"SELECT {Users.COLUMN_ACCOUNT_ID} FROM {Users.TABLE_NAME} WHERE {Users.COLUMN_USERID} ='{username}' AND {Users.COLUMN_PASSWORD} = '{password}';"
            )

        except Exception as e:
            Log.error(__file__, str(e))
        if cursor is not None:  # no error occurred
            records = cursor.fetchall()  # NOT USING FETCHONE AS IT WAS RETURNING ERROR
            if len(records) == 0:  # Wrong user
                onValidated(False)
                return
            else:

                for i in self.__onUserValidatedFunctions:
                    i(records[0][0])

                onValidated(True)

