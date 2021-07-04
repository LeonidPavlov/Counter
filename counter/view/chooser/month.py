import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime as dt

from counter.model.index import month_name
from counter.view.chooser.year import Year

x = 4
y = 3

class Month:
    def __init__(self, boss: tk.Tk, rim: ttk.LabelFrame, 
                    year: Year, month_change_listener) -> None:
        self.__boss = boss
        self.__rim = rim
        self.__year = year
        self.__month_change_listener = month_change_listener

        ttk.Button(self.__rim, text = '<<', width = min, 
                    command = self.rewind_left)\
                    .grid(column=0, row=1, padx=x, pady=y)
        ttk.Label(self.__rim, textvariable = self.__boss.month_name, width=9)\
                    .grid(column = 1, row = 1, padx=x, pady=y)
        self.__set_month_name()
        ttk.Label(self.__rim, textvariable = self.__boss.number)\
                    .grid(column = 2, row = 1)
        ttk.Label(self.__rim, textvariable = self.__boss.month, width = 2)\
                    .grid(column = 3, row = 1, padx=x, pady=y)
        ttk.Button(self.__rim, text = '>>', width = min, 
                    command = self.rewind_right)\
                    .grid(column = 4, row = 1, padx=x, pady=y)
    
    def rewind_left(self) -> None:
        if self.__boss.month.get() > 0:
            self.__boss.month.set(self.__boss.month.get() - 1)
        if self.__boss.month.get() == 0:
            self.__boss.month.set(12)
            self.__year.rewind_year_left()
        self.__set_month_name()
        self.__month_change_listener()
    
    def rewind_right(self) -> None:
        if self.__boss.month.get() <= 12:
            self.__boss.month.set(self.__boss.month.get() + 1)
        if self.__boss.month.get() == 13:
            self.__boss.month.set(1)
            self.__year.rewind_year_right()
        self.__set_month_name()
        self.__month_change_listener()

    def __set_month_name(self) -> None:
        self.__boss.month_name.set(month_name[self.__boss.month.get()])
    