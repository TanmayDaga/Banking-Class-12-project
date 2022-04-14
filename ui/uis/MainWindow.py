import threading
import time

from ui.constants_ui import WIDTH, HEIGHT, CODE_SPLASHSCREEN, CODE_LOGIN_WINDOW, CODE_USER_INTERFACE, \
    CODE_TRANSACTION_PAGE, CODE_TRANSACTION_SUCCESSFUL_PAGE, CODE_TRANSACTION_UNSUCCESSFUL_PAGE, \
    CODE_DETAILS_UPDATE_UNSUCCESSFUL, CODE_DETAILS_UPDATE_PAGE, CODE_DETAILS_UPDATE_SUCCESSFUL
import tkinter as tk
from ui.dataholders import LoginWindowViewModel, UserInterfaceViewModel
from ui.uis import SplashScreen, LoginWindow, UserInterface, TransactionPage, TransactionSuccessful, \
    TransactionUnsuccessful, UpdatePage, UpdateSuccessful, UpdateUnsuccessful
from Repository import Repository


class MainWindow(tk.Tk):
    curUserId: int = None
    width = WIDTH
    height = HEIGHT

    codeToClass: dict = {
        CODE_SPLASHSCREEN: SplashScreen.SplashScreen,
        CODE_LOGIN_WINDOW: LoginWindow.UserLogin,
        CODE_USER_INTERFACE: UserInterface.UserInterface,
        CODE_TRANSACTION_PAGE: TransactionPage.TransactionPage,
        CODE_TRANSACTION_SUCCESSFUL_PAGE: TransactionSuccessful.TransactionSuccessful,
        CODE_TRANSACTION_UNSUCCESSFUL_PAGE: TransactionUnsuccessful.TransactionUnsuccessful,
        CODE_DETAILS_UPDATE_PAGE: UpdatePage.UpdatePage,
        CODE_DETAILS_UPDATE_SUCCESSFUL: UpdateSuccessful.UpdateSuccessful,
        CODE_DETAILS_UPDATE_UNSUCCESSFUL: UpdateUnsuccessful.UpdateUnsuccessful
    }

    def __init__(self):
        super(MainWindow, self).__init__()
        self.geometry(f"{WIDTH}x{HEIGHT}")  # Setting geometry
        self.title("Banking")
        self.resizable(False, False)

        LoginWindowViewModel.LoginWindowViewModel.get_instance().addValidateUserObserver(self.__onUserIdChanged)
        SplashScreen.SplashScreen(self)

    def transition(self, caller, UiCode):
        """
        The transition function is used to transition between the different
        UiCodes. It is called by the main menu and takes in a UiCode as well as
        the current user id. The function then destroys caller, calling its
        destroy method, and creates an instance of the class that corresponds to
        the UiCode it was given.

        :param self: Used to Access variables that belongs to the class.
        :param caller: Used to Pass the current object to the next object.
        :param UiCode: Used to Determine which class to instantiate.
        """

        if UiCode is None:
            self.destroy()
        caller.destroy()
        self.codeToClass[UiCode](self)

    def __onUserIdChanged(self, newUserId):
        self.curUserId = newUserId






