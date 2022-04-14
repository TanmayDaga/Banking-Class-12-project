from Repository import Repository
from ui.uis.MainWindow import MainWindow

Repository.get_instance().setDbHelper("localhost", "root", "TanmayDaga")  # Initialising Database
app = MainWindow()

app.mainloop()