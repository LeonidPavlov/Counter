import tkinter as tk
from tkinter.constants import CENTER
import tkinter.ttk as ttk
from datetime import datetime as dt

from counter.aux.error_handling import ACHTUNG
from counter.view.chooser.year import Year

class Chooser:
    def __init__(self, boss: tk.Tk, rim: ttk.LabelFrame) -> None:
        self.__rim = rim
        Year(boss, rim)

    def instance(self) -> ttk.LabelFrame:
        return self.__rim

