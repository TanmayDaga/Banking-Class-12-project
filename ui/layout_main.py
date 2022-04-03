import tkinter as tk

from layout_splash_screen import SplashScreen



if __name__ == '__main__':
    root = tk.Tk()
    root.title("hello World")
    root.geometry("400x400")
    sp = SplashScreen(root)

    root.mainloop()
