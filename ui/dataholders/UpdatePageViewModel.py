from Log import Log
from typing import Callable
from Repository import Repository
from Database.Entities.Account import Accounts


class UpdateViewModel:
    __instance = None
    @staticmethod
    def get_instance() -> 'UpdateViewModel':  # Used string as class doesn't exist at the time of parsing
        """
        The get_instance method is a static method maintaining and returning only single instance of class
        implementing singleton method
        :param:.
        :return: UpdateViewModel class Instance.
        """
        if UpdateViewModel.__instance is None:
            UpdateViewModel.__instance = UpdateViewModel()
            Log.info(__file__, "UpdatePageViewModel Created")
        return UpdateViewModel.__instance

    def updateData(self, curUserId, data: list[str, str, int], onUpdationCompleteFunc: Callable[[bool], None]):

        """
        The updateData function updates the data of a particular user in the database.
        The function takes in 4 parameters:
            1) curUserId - The id of the user whose data is to be updated.
            2) data - A list containing 3 strings and an integer, which are to be updated as follows:
                [account_holder_address, account_email_id, account_phoneNumber]

            3) onUpdationCompleteFunc - A callback function that is called when updation has been completed successfully or not.

        :param self: Used to Access the class properties.
        :param data:list[str,str,int]: Used to Store the data that is to be updated.
        :param onUpdationCompleteFunc:Callable[[bool],None]: Used to Notify the caller about the updation status.
        :return:.
        """
        try:
            # No need to use cursor as updating data
            Repository.get_instance().execute(f"UPDATE {Accounts.TABLE_NAME} set "
                                              f"{Accounts.COLUMN_ACCOUNT_HOLDER_ADDRESS} = '{data[0]}',"
                                              f"{Accounts.COLUMN_ACCOUNT_EMAIL_ID} = '{data[1]}',"
                                              f"{Accounts.COLUMN_ACCOUNT_PHONE_NUMBER} = {data[2]} "
                                              f"WHERE {Accounts.COLUMN_ACCOUNTS_ID} = {curUserId};")

        except Exception as e:
            Log.error(__file__, str(e))
            onUpdationCompleteFunc(False)

        onUpdationCompleteFunc(True)


