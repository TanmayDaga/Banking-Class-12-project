import threading
import tkinter as tk
from Repository import Repository
from Log import Log


class UserInterface(tk.Frame):
    """The class is inherited from tk.Frame and creates the required frame"""

    def __init__(self, root, userid: int):
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

        self.__userId: int = userid
        self.__balanceAmount: float = 0.0  # Using Later
        self.__userIdText = tk.StringVar()
        self.__userIdEntry = tk.Entry(self, textvariable=self.__userIdText)
        self.__userIdEntry.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        self.__balanceAmountLabel = tk.Label(self, justify="left")
        self.__balanceAmountLabel.grid(row=0, column=1)

        self.__buttonLogOut = tk.Button(self, text="Log Out")
        self.__buttonLogOut.grid(row=0, column=2, sticky="e")

        self.__personalDetailsLabel = tk.Label(self, text="Personal Details")
        self.__personalDetailsLabel.grid(row=1, column=0, sticky="w", padx=10)

        # Dob
        self.__dobLabel = tk.Label(self)
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

        #   ----------Personal Details Not Editable---------------

        # Address
        self.__addressLabel = tk.Label(self, text="Address")
        self.__addressLabel.grid(row=6, column=0, sticky="w", padx=10)

        self.__addressText = tk.StringVar()
        self.__addressEntry = tk.Entry(self, textvariable=self.__addressText, justify="left")
        self.__addressEntry.grid(row=6, column=1)

        # Phone number
        self.__phoneNumberLabel = tk.Label(self, text="Phone Number")
        self.__phoneNumberLabel.grid(row=7, column=0, sticky="w", padx=10)

        self.__phoneNumberText = tk.IntVar()
        self.__phoneNumberEntry = tk.Entry(self, textvariable=self.__phoneNumberText, justify="left")
        self.__phoneNumberEntry.grid(row=7, column=1)

        #     Email Id
        self.__emailIdLabel = tk.Label(self, text="Email Id")
        self.__emailIdLabel.grid(row=8, column=0, sticky="w", padx=10)

        self.__emailText = tk.StringVar()
        self.__emailEntry = tk.Entry(self, textvariable=self.__emailText, justify="left")
        self.__emailEntry.grid(row=8, column=1)

        self.__transactButton = tk.Button(master=self, text="Transact Amount")
        self.__transactButton.grid(row=9, column=0, sticky="w", padx=10, pady=5)

        self.__submitButton = tk.Button(master=self, text="Submit Details")
        self.__submitButton.grid(row=9, column=1, sticky="e", pady=5)

        populateUiThread = threading.Thread(target=self.__populateUi)
        populateUiThread.start()

    def __populateUi(self):
        """
        The __populateUi function populates the user interface with data from the database.
        It takes no arguments and returns nothing.

        :param self: Used to Access variables that belongs to the class.
        :return:.
        """

        cursor = Repository.get_instance().getDataById(self.__userId)
        records = cursor.fetchone()

        Log.info(__file__, f"{records}")

        self.__userIdText.set("User Id: " + records[0])
        self.__dobLabel.configure(text="D.O.B: " + str(records[1]))  # Date object so converting to string
        self.__addressText.set(records[2])
        self.__phoneNumberText.set(records[3])
        self.__emailText.set(records[4])
        self.__balanceAmount = float(records[5])
        self.__balanceAmountLabel.configure(text="Balance: " + str(self.__balanceAmount))  # Decimal object to str
        self.__accountOpenLabel.configure(
            text="Account open Date: " + str(records[6]))  # Date object so converting to string
        self.__otherDetailsLabel.configure(text="Other Details: " + records[7])
        self.__accountTypeLabel.configure(
            text="Account Type: " + Repository.get_instance().getDescriptionOfAccountType(records[8]))

    def setTransactButtonOnClickListener(self, functon: callable):
        """
        The setTransactButtonOnClickListener function sets the onClickListener for the transact button.
        The function takes in a callable object as an argument, and sets that object as the onClickListener for
        the transact button. The function is called by passing in a lambda expression.

        :param self: Used to Access the attributes and methods of the class in python.
        :param functon:callable: Used to Pass a function to the settransactbuttononclicklistener method.
        :return: .

        """

        self.__transactButton.configure(command=functon)

    def getUserId(self) -> int:
        return self.__userId

    def getBalance(self) -> float:
        return self.__balanceAmount
