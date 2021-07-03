import tkinter as tk
from tkinter.constants import CENTER
import tkinter.ttk as ttk
from datetime import datetime as dt

from counter.aux.error_handling import ACHTUNG

class Year:
    def __init__(self, boss: tk.Tk, rim: tk.LabelFrame) -> None:
        self.__boss = boss
        self.__rim = rim

        self.__year_label: ttk.Label = ttk.Label(self.__rim, text = 'year')\
                    .grid(column = 1, row = 0)
        self.__rewind_left: ttk.Button = ttk.Button(self.__rim, text = '<<',
                 width = min, command = self.__rewind_year_left)\
                    .grid(column = 0, row = 1)
        self.__year_textbox: ttk.Entry = ttk.Entry(self.__rim,  width = 6, 
                    textvariable = self.__boss.year, justify = tk.CENTER)\
                    .grid(column = 1, row = 1)
        self.__rewind_right: ttk.Button = ttk.Button(self.__rim, 
                    text = '>>', width = min, 
                    command = self.__rewind_year_right)\
                    .grid(column = 2, row = 1)

    
    def __rewind_year_left(self) -> None:
        try:            
            if  self.__boss.year.get() is not str and\
                self.__boss.year.get() > 1 :
                self.__boss.year.set(self.__boss.year.get() - 1)
        except tk.TclError as err:
            ACHTUNG(err ,__file__, '__rewind_year_left method').console()
            self.__defend_year_value()

    def __rewind_year_right(self) -> None:
        try:
            if  self.__boss.year.get() is not str and\
                self.__boss.year.get() < 9999:
                self.__boss.year.set(self.__boss.year.get() + 1)
        except tk.TclError as err:
            ACHTUNG(err ,__file__, '__rewind_year_right method').console()
            self.__defend_year_value()

    def __defend_year_value(self) -> None:
        self.__boss.year.set(dt.now().year)
