import threading
import tkinter as tk
from tkinter import ttk
from Repository import Repository
from Log import Log


class TransactionPage(tk.Frame):
    """The class is inherited from tk.Frame and creates the required frame"""
    __userId: int

    def __init__(self, root, userid: int, balance: float):  # Not use type hinting for root as Circular import error
        """
        Initialises the ui of the frame and data

        :param self: Used to Refer to the object.
        :param root: App class instance.
        :param userid:int: Current Logged user id.
        :return: :.

        """

        super().__init__(master=root, width=500, height=500)

        self.pack(fill="both", expand=True, anchor="center")

        self.__userId = userid
        self.__balance = balance

        # Row 0

        self.__transactLabel = tk.Label(self, text="Transaction in progress")
        self.__transactLabel.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Row 1
        self.__toUserName = tk.Label(self,text="Transfer Amount To")
        self.__toUserName.grid(row=1, column=0, padx=10, sticky="w")

        self.__selectedUser = tk.StringVar()

        self.__toUserNameCombobox = ttk.Combobox(self, state="readonly", textvariable=self.__selectedUser)
        self.__toUserNameCombobox.grid(row=1, column=1)

        # Row 2
        self.__transactAmountLabel = tk.Label(self, text="Transaction Amount: ")
        self.__transactAmountLabel.grid(row=2, column=0, sticky="w", padx=10)

        self.__transactAmountText = tk.DoubleVar()
        # % P = value of the entry if the edit is allowed
        # %s = value of entry prior to editing
        vcmd = (self.register(self.__validateAmount), "%P", "%s")
        self.__transactAmountEntry = tk.Entry(self, textvariable=self.__transactAmountText, validate="key",
                                              validatecommand=vcmd)
        self.__transactAmountEntry.grid(row=2, column=1)

        # Row 3
        self.__transactTypeLabel = tk.Label(self, text="Transaction type")
        self.__transactTypeLabel.grid(row=3, column=0, sticky="w", padx=10)

        self.__transactType = tk.StringVar()
        self.__transactTypeCombobox = ttk.Combobox(self, state="readonly", textvariable=self.__transactType)
        self.__transactTypeCombobox.grid(row=3, column=1)

        # Row 4
        self.__transactFinalButton = tk.Button(self, text="Proceed")
        self.__transactFinalButton.grid(row=4, column=1, sticky="e")

        thread = threading.Thread(target=self.__populateUi)
        thread.start()

    def __populateUi(self) -> None:
        """
        The __populateUi function populates the user interface with data from the database.
        The function uses a list of users, which are retrieved from the database using
        the getOtherUsersForTransactions method in Repository class, and adds them to a combobox widget.
        The transaction types are also retrieved using getTransactionTypes,and are added  to the combobox widget.

        :param self: Used to Access variables that belongs to the class.
        :return:.

        """

        # Creating new variable cause there required lists references are passed to entry
        # using .set as directly setting will reassign variable
        userList = Repository.get_instance().getOtherUsersForTransactions(self.__userId)
        self.__toUserNameCombobox['values'] = userList
        self.__selectedUser.set(userList[0])

        transactionTypeList = Repository.get_instance().getTransactionTypes()
        self.__transactTypeCombobox['values'] = transactionTypeList
        self.__transactType.set(transactionTypeList[0])

    def __validateAmount(self, valueFinal, valuePrior) -> bool:
        Log.info(__file__, "Validate amount called")
        if valueFinal == "" or valueFinal is None:
            return True
        try:
            if (float(valueFinal) <= self.__balance):
                return True
        except ValueError:
            pass
        return False
