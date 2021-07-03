import tkinter as tk
from tkinter.constants import CENTER
import tkinter.ttk as ttk
from datetime import datetime as dt

from counter.aux.error_handling import ACHTUNG
from counter.model.index import month_name
class Year:
    def __init__(self, boss: tk.Tk, rim: tk.LabelFrame) -> None:
        self.__boss = boss
        self.__rim = rim

        ttk.Label(self.__rim, text = 'year').grid(column = 1, row = 0)
        ttk.Button(self.__rim, text = '<<',width = min, 
                    command = self.rewind_year_left)\
                    .grid(column = 0, row = 1)
        ttk.Label(self.__rim, textvariable = self.__boss.year)\
                    .grid(column = 1, row = 1, columnspan = 2)
        ttk.Button(self.__rim, text='>>', width = min,
                command = self.rewind_year_right)\
                    .grid(column=3, row=1)

    def rewind_year_left(self) -> None:
        if  self.__boss.year.get() > 1 :
            self.__boss.year.set(self.__boss.year.get() - 1)

    def rewind_year_right(self) -> None:
        if  self.__boss.year.get() < 9999:
            self.__boss.year.set(self.__boss.year.get() + 1)

