from tkinter import *
from tkinter import ttk

from counter.view.action_pane import Action_Pane
from counter.view.selection_pane import Selection_Pane

class App(Tk):
    def __init__(self, *args, **kwards) -> None:
        Tk.__init__(self, *args, **kwards)
        self.title('EBANAFTUMBA')
        self.grid()
        self.__main_frame = ttk.Frame(self)
        self.__main_frame.grid(column=0, row=0, sticky=(W, N, E, S))
        Action_Pane(self.__main_frame)
        Selection_Pane(self.__main_frame)
    def start(self):
        self.mainloop()

    def stop(self) -> None:
        self.destroy()
        
