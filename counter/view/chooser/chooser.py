import tkinter as tk
from tkinter.constants import CENTER
import tkinter.ttk as ttk
from datetime import datetime as dt

from counter.aux.error_handling import ACHTUNG
from counter.view.chooser.day import Day
from counter.view.chooser.month import Month
from counter.view.chooser.year import Year

class Chooser:
    def __init__(self, boss: tk.Tk, rim: ttk.LabelFrame) -> None:
        self.__boss = boss
        self.__rim = rim
        year = Year(boss, rim, self.__year_change_Listener)
        month = Month(boss, rim, year, self.__month_change_listener)
        self.__day = Day(boss, rim, month)

    def instance(self) -> ttk.LabelFrame:
        return self.__rim

    def __year_change_Listener(self):
        self.__day.on_change_year_do_something()

    def __month_change_listener(self):
        self.__day.on_change_month_do_something()
