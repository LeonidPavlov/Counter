from tkinter import *
from tkinter import ttk
from datetime import datetime as dt

from counter.model.index import column_name, Fields as f, Order as o

class Selection_Pane(ttk.LabelFrame):

    def __init__(self, parent: ttk.Frame, *args, **kwards) -> None:
        super().__init__(parent, text = 'selection')
        self.grid(column = 1, row = 0, sticky = (N, S))
        

        var = StringVar(self)
        self.__items = []

        for j in range(len(column_name))[1 :]:
            l = ttk.Label(self, text = column_name[j].lower())
            l.grid(column = 0, row = j - 1)
            c = ttk.Combobox(self, textvariable = column_name[j].lower())
            c.grid(column = 1, row = j - 1)


    def ebumba(self) -> None:
        print("EBUMBA")    


if __name__ == '__main__':
    for j in range(len(column_name))[1 :]:    
        print(column_name[j].lower())

