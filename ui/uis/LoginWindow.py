import tkinter as tk
from Log import Log
from tkinter import ttk

from ui.dataholders.LoginWindowViewModel import LoginWindowViewModel

from ui.constants_ui import CODE_USER_INTERFACE


class UserLogin(ttk.Frame):
    __nextUI_function: callable = None

    def __init__(self, root):
        super().__init__(master=root, width=500, height=500)

        self.pack(fill="both", expand=True, anchor="center")
        self.__root = root
        self.__initViews()

        Log.info(__file__, "UserLogin Frame Created")

    def __initViews(self):
        self.__loginLabel = tk.Label(master=self, text="Login")
        self.__loginLabel.grid(row=0, column=0, columnspan=2, sticky="n", pady=10)

        self.__userIdLabel = tk.Label(master=self, text="Id")
        self.__userIdLabel.grid(row=1, column=0)

        self.__userIdText = tk.StringVar()
        self.__idEntry = tk.Entry(master=self, textvariable=self.__userIdText)
        self.__idEntry.grid(row=1, column=1)

        self.__passwordIdLabel = tk.Label(master=self, text="Password")
        self.__passwordIdLabel.grid(row=2, column=0)

        self.__passwordText = tk.StringVar()
        self.__passwordEntry = tk.Entry(master=self, textvariable=self.__passwordText)
        self.__passwordEntry.grid(row=2, column=1)

        self.__submitButton = tk.Button(master=self, text="Submit")
        self.__submitButton.configure(
            command=lambda: LoginWindowViewModel.get_instance().validateUser(self.__userIdText.get(),
                                                                             self.__passwordText.get(),
                                                                             self.onUserValidation))

        self.__submitButton.grid(row=3, column=2)

    def destroy(self) -> None:
        Log.info(__file__, "User Login Frame Destroyed")
        super().destroy()

    def onUserValidation(self, isUser: bool):
        """
        The onUserValidation function is called when the user is validated.
        If isUser is false label sets the wrong text
        true value is handled by mainWindow

        :param self: Used to Access variables that belongs to the class.
        :param isUser:bool: Used to Check if the user is valid.
        :return: .
        """

        if not isUser:
            self.__loginLabel.configure(text="Wrong User Id")
        else:
            self.__root.transition(self, CODE_USER_INTERFACE)
