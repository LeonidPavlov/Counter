
from tkinter import *
from tkinter import ttk
import shutil


class Main_Frame(ttk.Frame):
    def __init_(self, parent: Tk, *args, **kwards):
        self.__parent = parent
        self.configure(parent)
        self.grid(column=0, row=0, sticky=(W, N, E, S))

    def get_parent(self) -> Tk:
        return self.__parent

class App(Tk):
    def __init__(self, *args, **kwards) -> None:
        Tk.__init__(self, *args, **kwards)
        self.title('EBANAFTUMBA')
        Main_Frame()
        self.mainloop()

    def stop(self) -> None:
        self.destroy()

