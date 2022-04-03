import tkinter as tk
from PIL import Image, ImageTk

from Log import Log
class SplashScreen:
    def __init__(self, master):
        myFrame = tk.Frame(master)
        myFrame.place(anchor="center")
        myFrame.pack()

        (width,height) = master.size()
        Log.info(__file__,f"{width},{height}")

        img = ImageTk.PhotoImage(Image.open("Image Assests/splash_background.jpg"))

        #
        # img = Image.open("Image Assests/splash_background.jpg")
        # img = ImageTk.PhotoImage(img)
        self.imageLabel = tk.Label(myFrame, image=img)
        self.imageLabel.image = img

        self.imageLabel.pack(pady=20)
