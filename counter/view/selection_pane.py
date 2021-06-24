from tkinter import *
from tkinter import ttk

_choise = ( 'balance', 'type', 'source', 'category', 'product', 'year',
            'month', 'day', 'hour', 'minute', 'cost', 'amount', 'total')

class Selection_Pane(ttk.LabelFrame):

    def __init__(self, parent: ttk.Frame, *args, **kwards) -> None:
        super().__init__(parent, text = 'selection')
        self.grid(column = 1, row = 0, sticky = (N, S))

        var = StringVar(self)
        self.__items = {}

        for j in range( len(_choise) ):
            pass #compobox


