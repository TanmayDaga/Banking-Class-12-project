import threading
import tkinter as tk
from tkinter import ttk
from Repository import Repository
from Log import Log

from ui.dataholders.TransactPageViewModel import TransactPageViewModel

from ui.constants_ui import CODE_TRANSACTION_SUCCESSFUL_PAGE, CODE_TRANSACTION_UNSUCCESSFUL_PAGE


class TransactionPage(tk.Frame):
    """The class is inherited from tk.Frame and creates the required frame"""
    __userId: int

    def __init__(self, root):  # Not use type hinting for root as Circular import error
        """
        Initialises the ui of the frame and data

        :param self: Used to Refer to the object.
        :param root: App class instance.
        :param userid:int: Current Logged user id.
        :return: :.

        """

        super().__init__(master=root, width=500, height=500)
        self.__root = root
        self.pack(fill="both", expand=True, anchor="center")

        self.__initViews()

        Log.info(__file__,"TransactionPageFrame Created")
        TransactPageViewModel.get_instance().getUsers(self.__root.curUserId, self.__onUpdateUsers)
        TransactPageViewModel.get_instance().getTransactionTypes(self.__onUpdateTransactionTypes)

    def __initViews(self):

        # Row 0

        self.__transactLabel = tk.Label(self, text="Transaction in progress")
        self.__transactLabel.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Row 1
        self.__toUserName = tk.Label(self, text="Transfer Amount To")
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
        self.__transactFinalButton.configure(command=
                                             lambda: TransactPageViewModel.get_instance()
                                             .startTransaction(self.__root.curUserId, self.__selectedUser.get(),
                                                               self.__transactAmountText.get(),
                                                               self.__transactType.get(),
                                                               self.__onTransactionCompleted))
        self.__transactFinalButton.grid(row=4, column=1, sticky="e")

    def __onUpdateUsers(self, userList: list):

        self.__toUserNameCombobox['values'] = userList
        self.__selectedUser.set(userList[0])

    def __onUpdateTransactionTypes(self, transactionTypesList: list):
        self.__transactTypeCombobox['values'] = transactionTypesList
        self.__transactType.set(transactionTypesList[0])

    def __validateAmount(self, valueFinal, valuePrior) -> bool:

        Log.info(__file__, "Validate amount called")
        if valueFinal == "" or valueFinal is None:
            return True
        try:
            float(valueFinal)
            return True
        except ValueError:
            pass
        return False

    def __onTransactionCompleted(self, isSuccesful: bool,msg):
        uiCode = CODE_TRANSACTION_UNSUCCESSFUL_PAGE
        if isSuccesful: uiCode = CODE_TRANSACTION_SUCCESSFUL_PAGE
        self.__root.transition(self, uiCode)

    def destroy(self) -> None:
        Log.info(__file__, "TransactionPageFrame Destroyed")
        super().destroy()
