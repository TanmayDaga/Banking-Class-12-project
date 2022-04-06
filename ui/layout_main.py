import threading
import time
import tkinter as tk
from ui.constant_ui import *

from Log import Log




class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setting Window Properties (widthxheight)
        self.geometry(f"{WIDTH_WINDOW}x{HEIGHT_WINDOW}")

        self.resizable(width=False, height=False)
        self.title(TITLE_WINDOW)
        Log.info(__file__, "MainWindow Created")



