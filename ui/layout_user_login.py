import tkinter as tk
from Log import Log
from ui.constant_ui import *


class UserLogin(tk.Frame):
    __validator_function: callable = None
    __nextUI_function: callable = None

    def __init__(self, root):
        super().__init__(master=root, width=500, height=500)

        self.pack(fill="both", expand=True, anchor="center")

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

        self.__submitButton = tk.Button(master=self, text="Submit", command=self.onSubmitClick)
        self.__submitButton.grid(row=3, column=2)

    def setValidatorFunction(self, fxn: callable):
        self.__validator_function = fxn

    def setNextUiFunction(self, fxn: callable):
        self.__nextUI_function = fxn

    def onSubmitClick(self):
        (isCorrect, userId) =  self.__validator_function(self.__userIdText.get(), self.__passwordText.get())
        if isCorrect:
            Log.info(__file__, f"UserId : {userId}")
            self.__loginLabel.configure(text="Login")
            self.__nextUI_function(userId)

        else:
            self.__loginLabel.configure(text="Wrong user id or password")

    def destroy(self) -> None:
        Log.info(__file__, "User Login Frame Destroyed")
        super().destroy()
