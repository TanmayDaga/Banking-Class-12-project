import threading
import time

from Repository import Repository
from ui.constant_ui import *
from ui.layout_main import App
from ui.layout_splash_screen import SplashScreen
from ui.layout_user_login import UserLogin
from ui.layout_user_interface import UserInterface
from ui.layout_transact_amount import TransactionPage


def initialise():
    initialiseDb()
    initialiseFrame()


def initialiseDb():
    Repository.get_instance().setDbHelper("localhost", "root", "TanmayDaga")


def transactBtnFunc():
    global root, ui, tp
    userId = ui.getUserId()
    balance = ui.getBalance()
    ui.destroy()
    tp = TransactionPage(root, userId,balance)
    


def nextUiFunc(userId: int):
    global ul, root, ui

    ul.destroy()
    ui = UserInterface(root, userId)
    ui.setTransactButtonOnClickListener(transactBtnFunc)


def initialiseFrame():
    global ul, root

    sp = SplashScreen(root)
    time.sleep(SPLASHSCREEN_DELAY_SECONDS)
    sp.destroy()
    ul = UserLogin(root)
    ul.setValidatorFunction(Repository.get_instance().validator)
    ul.setNextUiFunction(nextUiFunc)


if __name__ == '__main__':
    ul: UserLogin
    ui: UserInterface
    tp: TransactionPage
    root: App
    root = App()

    thread = threading.Thread(target=initialise)  # Using threading to prevent blocking of main thread
    thread.start()

    root.mainloop()
