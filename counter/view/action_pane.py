from tkinter import *
from tkinter import ttk

from counter.view.selection_pane import Selection_Pane

_pad_x = 20
_pad_y = 10

class Action_Pane(ttk.LabelFrame):
    
    def __init__(self, parent: ttk.Frame, selection_pane:Selection_Pane,
                *args, **kwards,) -> None: 
        super().__init__(parent, text='action')
        self.grid(column=0, row=0, sticky=(W,N,E,S))
        
        self.__new_button = ttk.Button(self, text = 'new', 
                        command = selection_pane.set_new_variants)
        self.__new_button.grid(column = 0, row = 0, 
                                padx = _pad_x, pady = _pad_y)

        