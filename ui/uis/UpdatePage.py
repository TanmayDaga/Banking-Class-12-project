# TODO = To complete the class
from tkinter import ttk
from Log import Log
import tkinter as tk
from ui.dataholders.UpdatePageViewModel import UpdateViewModel

from ui.constants_ui import CODE_DETAILS_UPDATE_SUCCESSFUL, CODE_DETAILS_UPDATE_UNSUCCESSFUL, CODE_USER_INTERFACE


class UpdatePage(ttk.Frame):
    __nextUI_function: callable = None

    def __init__(self, root):
        super().__init__(master=root, width=500, height=500)

        self.pack(fill="both", expand=True, anchor="center")
        self.__root = root
        self.__initViews()

        Log.info(__file__, "UpdatePage Frame Created")

    def __initViews(self):
        # Address
        self.__addressLabel = tk.Label(self, text="Address")
        self.__addressLabel.grid(row=0, column=0, sticky="w", padx=10)

        self.__addressText = tk.StringVar()
        self.__addressEntry = tk.Entry(self, textvariable=self.__addressText, justify="left")
        self.__addressEntry.grid(row=0, column=1)

        # Phone number
        self.__phoneNumberLabel = tk.Label(self, text="Phone Number")
        self.__phoneNumberLabel.grid(row=1, column=0, sticky="w", padx=10)

        self.__phoneNumberText = tk.IntVar()
        self.__phoneNumberEntry = tk.Entry(self, textvariable=self.__phoneNumberText, justify="left")
        self.__phoneNumberEntry.grid(row=1, column=1)

        #     Email Id
        self.__emailIdLabel = tk.Label(self, text="Email Id")
        self.__emailIdLabel.grid(row=2, column=0, sticky="w", padx=10)

        self.__emailText = tk.StringVar()
        self.__emailEntry = tk.Entry(self, textvariable=self.__emailText, justify="left")
        self.__emailEntry.grid(row=2, column=1)

        self.__submitButton = tk.Button(master=self, text="Submit Details", command=self.__submitOnClickListener)
        self.__submitButton.grid(row=3, column=1, sticky="e", pady=5)

    def __submitOnClickListener(self):
        UpdateViewModel.get_instance().updateData(
            self.__root.curUserId, [self.__addressText.get(), self.__emailText.get(), self.__phoneNumberText.get()],
            self.onUpdationComplete
        )

    def onUpdationComplete(self, updationSuccessful: bool):
        """
        The onUpdationComplete function is called when the details have been fetched from database.
        It takes in a boolean parameter, updationSuccessful, which indicates whether the update was successful or not.

        :param self: Used to Access the class attributes and methods.
        :param updationSuccessful:bool: Used to Check if the updation was successful or not.
        :return: .
        """

        uiCode = CODE_DETAILS_UPDATE_SUCCESSFUL if updationSuccessful else CODE_DETAILS_UPDATE_UNSUCCESSFUL

        self.__root.transition(self, uiCode)

    def destroy(self) -> None:
        Log.info(__file__, "UpdatePage Frame Destroyed")
        super().destroy()
