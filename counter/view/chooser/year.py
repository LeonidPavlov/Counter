import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime as dt

from counter.aux.error_handling import ACHTUNG
from counter.model.index import month_name


class Year:
    def __init__(self, boss: tk.Tk, rim: tk.LabelFrame, 
                    year_change_listener: object) -> None:
        self.__boss = boss
        self.__rim = rim
        self.__year_change_listener = year_change_listener
        ttk.Button(self.__rim, text = '<<',width = min, 
                    command = self.rewind_year_left)\
                    .grid(column = 0, row = 0, pady = 3)
        ttk.Label(self.__rim, textvariable = self.__boss.year)\
                    .grid(column = 1, row = 0, columnspan = 3)
        ttk.Button(self.__rim, text='>>', width = min,
                command = self.rewind_year_right)\
                    .grid(column=4, row=0)

    def rewind_year_left(self) -> None:
        if  self.__boss.year.get() > 1 :
            self.__boss.year.set(self.__boss.year.get() - 1)
            self.__year_change_listener()

    def rewind_year_right(self) -> None:
        if  self.__boss.year.get() < 9999:
            self.__boss.year.set(self.__boss.year.get() + 1)
            self.__year_change_listener()
