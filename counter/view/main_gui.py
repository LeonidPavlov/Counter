from tkinter import *
from tkinter import ttk
from datetime import datetime as dt

from counter.view.actions import Actions
from counter.view.chooser.chooser import Chooser
from counter.view.selection_pane import Selection_Pane

pad_x = 10 
pad_y = 5

class App(Tk):
    def __init__(self, *args, **kwards) -> None:
        Tk.__init__(self, *args, **kwards)
        self.title('counter')
        self.grid()
        self.__frame = ttk.Frame(self)
        self.__variables()
        self.__frame.grid(column=0, row=0, sticky=(W, N, E, S))
        
        actions = Actions(self, ttk.LabelFrame\
                            (self.__frame, text = 'actions'))    
        actions.instance().grid(column = 0, row = 0, padx = pad_x, 
                pady = pad_y)
        
        chooser = Chooser(self, ttk.LabelFrame\
                        (self.__frame, text = 'date & time'))
        chooser.instance().grid(column = 0, row = 1, 
                                    padx = pad_x, pady = pad_y)
        
        self.mainloop()

    def __variables(self) -> None:
        self.year = IntVar(value = dt.now().year)
        self.month = IntVar(value = dt.now().month)
        self.month_name = StringVar(value = 'month')
        self.number = StringVar(value = '№')
        self.day = IntVar(value = dt.now().day)
        self.day_name = StringVar(value = 'monday')