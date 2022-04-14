import threading
import tkinter as tk
from Repository import Repository
from Log import Log
from ui.dataholders.UserInterfaceViewModel import UserInterFaceModel

from ui.constants_ui import CODE_TRANSACTION_PAGE, CODE_DETAILS_UPDATE_PAGE, CODE_LOGIN_WINDOW


class UserInterface(tk.Frame):
    """The class is inherited from tk.Frame and creates the required frame"""

    def __init__(self, root):
        """
        The __init__ function is called when an instance of the class is created.
        It initializes variables that are common to all instances of the class.
        The self parameter refers to the current instance of the class.

        :param self: Used to Refer to the object.
        :param root: App class instance.
        :param userid:int: Current Logged user id.
        :return: :.

        """

        super().__init__(master=root, width=500, height=500)

        self.pack(fill="both", expand=True, anchor="center")
        self.__root = root
        Log.info(__file__, "User Interface Frame Created")
        self.__initViews()

    def __initViews(self):
        """
        The __initViews function creates the views for the user interface. It creates a grid layout with labels and
        entry boxes to display personal details of the user, such as name, address, phone number and email id. The
        function also creates buttons to allow users to log out or transact money.

        :param self: Used to Refer to the object from inside the class.
        :return: The following:.

        """
        self.__userIdText = tk.StringVar()
        self.__userIdEntry = tk.Entry(self, textvariable=self.__userIdText)
        self.__userIdEntry.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.__balanceAmountLabel = tk.Label(self, justify="left")
        self.__balanceAmountLabel.grid(row=0, column=1)

        self.__buttonLogOut = tk.Button(self, text="Log Out")
        self.__buttonLogOut.configure(command=lambda: self.__root.transition(self, CODE_LOGIN_WINDOW))
        self.__buttonLogOut.grid(row=0, column=2, sticky="e")

        self.__personalDetailsLabel = tk.Label(self, text="Personal Details")
        self.__personalDetailsLabel.grid(row=1, column=0, sticky="w", padx=10)

        # Dob
        self.__dobLabel = tk.Label(self, text="")
        self.__dobLabel.grid(row=2, column=0, sticky="w", padx=10)

        #     Account Open Date
        self.__accountOpenLabel = tk.Label(self)
        self.__accountOpenLabel.grid(row=3, column=0, sticky="w", padx=10)

        # AccountType
        self.__accountTypeLabel = tk.Label(self)
        self.__accountTypeLabel.grid(row=4, column=0, sticky="w", padx=10)

        # Other Details
        self.__otherDetailsLabel = tk.Label(self)
        self.__otherDetailsLabel.grid(row=5, column=0, sticky="w", padx=10)

        # Address
        self.__addressLabel = tk.Label(self, text="Address")
        self.__addressLabel.grid(row=6, column=0, sticky="w", padx=10)

        self.__addressTextLabel = tk.Label(self)
        self.__addressTextLabel.grid(row=6, column=1)

        # Phone number
        self.__phoneNumberLabel = tk.Label(self, text="Phone Number", justify="left")
        self.__phoneNumberLabel.grid(row=7, column=0, sticky="w", padx=10)

        self.__phoneNumberTextLabel = tk.Label(self, justify="left")
        self.__phoneNumberTextLabel.grid(row=7, column=1)

        #     Email Id
        self.__emailIdLabel = tk.Label(self, text="Email Id")
        self.__emailIdLabel.grid(row=8, column=0, sticky="w", padx=10)

        self.__emailTextLabel = tk.Label(self, justify="left")
        self.__emailTextLabel.grid(row=8, column=1)

        self.__transactButton = tk.Button(master=self, text="Transact Amount")
        self.__transactButton.configure(command=lambda: self.__root.transition(self, CODE_TRANSACTION_PAGE))
        self.__transactButton.grid(row=9, column=0, sticky="w", padx=10, pady=5)

        self.__updatePageButton = tk.Button(master=self, text="Update Details")
        self.__updatePageButton.configure(command=lambda: self.__root.transition(self, CODE_DETAILS_UPDATE_PAGE))
        self.__updatePageButton.grid(row=10, column=1, sticky="e", pady=5)

        UserInterFaceModel.get_instance().getData(self.__root.curUserId, self.onDataUpdated)

    def onDataUpdated(self, data: dict) -> None:
        """
        The function takes in a dictionary of data and sets the text of the labels and entry boxes to the values in the
        dictionary. To be called  when data updated
        :param data: dict
        :return: None
        """

        self.__userIdText.set(data[UserInterFaceModel.KEY_USER_NAME])
        self.__accountOpenLabel.configure(
            text="Account Open Date: " + str(data[UserInterFaceModel.KEY_ACCOUNT_OPEN_DATE]))  # would be a date object
        self.__accountTypeLabel.configure(text="Account Type: " + str(data[UserInterFaceModel.KEY_ACCOUNT_TYPE]))
        self.__balanceAmountLabel.configure(
            text="Balance Amount: " + str(data[UserInterFaceModel.KEY_BALANCE_AMOUNT]))  # would be decimal
        self.__personalDetailsLabel.configure(
            text="Other Details: " + str(data[UserInterFaceModel.KEY_ACCOUNT_OTHER_DETAILS]))
        self.__addressTextLabel.configure(text=data[UserInterFaceModel.KEY_USER_ADDRESS])
        self.__phoneNumberTextLabel.configure(text=data[UserInterFaceModel.KEY_PHONE_NUMBER])
        self.__emailTextLabel.configure(text=data[UserInterFaceModel.KEY_EMAIL_ID])

    def destroy(self) -> None:
        Log.info(__file__, "User Interface Frame Destroyed")
        super().destroy()
