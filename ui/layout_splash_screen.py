import tkinter as tk
from PIL import Image, ImageTk
from ui.constant_ui import *
from Log import Log


class SplashScreen(tk.Frame):
    def __init__(self, root):
        super().__init__(master=root)

        self.pack(fill="both", expand=True)
        self.__initViews()
        Log.info(__file__, "SplashScreen Frame Created")

    def __initViews(self):
        # Setting Background
        img = ImageTk.PhotoImage(Image.open("ui/Image Assests/splash_background.jpg").resize((WIDTH_WINDOW, HEIGHT_WINDOW),
                                                                                          Image.ANTIALIAS))
        self.imageLabel = tk.Label(self, image=img)
        self.imageLabel.image = img

        self.imageLabel.pack()

    def destroy(self) -> None:
        Log.info(__file__, "SplashScreen Frame Destroyed")
        super().destroy()
