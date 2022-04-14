import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from ui.constants_ui import *
from Log import Log


class SplashScreen(ttk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        self.pack(fill="both", expand=True)
        self.__initViews()
        self.__root = root
        Log.info(__file__, "SplashScreen Frame Created")
        self.after(4000, lambda: self.__root.transition(self, CODE_LOGIN_WINDOW))

    def __initViews(self):
        # Setting Background
        img = ImageTk.PhotoImage(
            Image.open("ui/Image Assests/splash_background.jpg").resize((WIDTH, HEIGHT),
                                                                        Image.ANTIALIAS))
        self.imageLabel = tk.Label(self, image=img)
        self.imageLabel.image = img

        self.imageLabel.pack()

    def destroy(self) -> None:
        Log.info(__file__, "SplashScreen Frame Destroyed")
        super().destroy()
