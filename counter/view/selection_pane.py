from tkinter import *
from tkinter import ttk
from datetime import datetime as dt

from counter.model.index import column_name, Fields as f, Order as o, \
            month_name

class Selection_Pane(ttk.LabelFrame):

    def __init__(self, parent: ttk.Frame, *args, **kwards) -> None:
        super().__init__(parent, text = 'selection')
        self.grid(column = 1, row = 0, sticky = (N, S))
        
        self.__items = []

        for j in range(len(column_name))[1 :]:

            l = ttk.Label(self, text = column_name[j].lower())
            l.grid(column = 0, row = j - 1, padx = 5, pady = 10)

            var = StringVar()
            var.set('')    
            c = ttk.Combobox(self, textvariable = var, width = 8)
            c.grid(column = 1, row = j - 1, padx = 5, pady = 10)

            self.__items.append((column_name[j],var,l, c))
        

    def set_new_variants(self) -> None:
        for item in self.__items:
            if item[0] == f.year.value:
                item[1].set(dt.now().year)
            if item[0] == f.month.value:
                item[1].set(month_name[dt.now().month])
            if item[0] == f.day.value:
                item[1].set(dt.now().day)
            if item[0] == f.hours.value:
                item[1].set(dt.now().hour)
                item[3]['values'] = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,\
                                        15, 16, 17, 18, 19, 20, 21, 22,23)
            if item[0] == f.balance.value:
                item[1].set('-')
                item[3]['values'] = ('+', '-', '=')
            if item[0] == f.minutes.value:
                item[1].set(dt.now().minute)
            if item[0] == f.minutes.value:
                item[1].set(dt.now().minute)
            if item[0] == f.minutes.value:
                item[1].set(dt.now().minute)

            