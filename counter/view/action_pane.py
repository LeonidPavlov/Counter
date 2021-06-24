from tkinter import *
from tkinter import ttk

actions = ('new', 'select', 'update' ,'delete', 'huysnim')

class Action_Pane(ttk.LabelFrame):
    
    
    def __init__(self, parent: ttk.Frame, *args, **kwards) -> None: 
        super().__init__(parent, text='action')
        self.grid(column=0, row=0, sticky=(W,N,E,S))
        
        self.__button_dict = {}
        for j in range(len(actions)):
            b = ttk.Button(self, text = actions[j], )
            b.grid(column = 0 , row = j,padx = 10, pady = 5)
            self.__button_dict[j] = {actions[j] : b}

        