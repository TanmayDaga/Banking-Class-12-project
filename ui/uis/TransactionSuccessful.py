import tkinter as tk
from PIL import Image, ImageTk
from ui.constants_ui import CODE_USER_INTERFACE, WIDTH, HEIGHT
from Log import Log


class TransactionSuccessful(tk.Frame):

    def __init__(self, root):
        super().__init__(master=root)
        self.__root = root
        self.pack(fill="both", expand=True)
        self.__initViews()
        Log.info(__file__, "TransactionSuccessful Frame Created")

    def __initViews(self):
        self.__backBtn = tk.Button(master=self, text="Back", command=
        lambda: self.__root.transition(self, CODE_USER_INTERFACE))

        self.__backBtn.pack(side=tk.TOP, anchor="w")

        img = ImageTk.PhotoImage(
            Image.open(
                "ui/Image Assests/transactSuccessfull.jpg").resize(
                (int(WIDTH / 2), int(HEIGHT / 2)),
                Image.ANTIALIAS))
        self.__imageLabel = tk.Label(self, image=img)
        self.__imageLabel.image = img

        self.__imageLabel.pack(anchor="center")

    def destroy(self) -> None:
        Log.info(__file__, "TransactionSuccessfulFrame Destroyed")
        super().destroy()
