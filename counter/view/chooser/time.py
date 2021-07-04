import tkinter as tk
from tkinter import ttk

x = 4
y = 3

from counter.view.chooser.day import Day

class Time:
    def __init__(self, boss: tk.Tk, rim: ttk.LabelFrame, day: Day) -> None:
        self.__boss = boss

        ttk.Separator(rim, orient = tk.HORIZONTAL).grid(column = 0, 
                            row = 3, columnspan = 5, sticky = (tk.E, tk.W))
        ttk.Label(rim, textvariable = boss.hours,
                            width = 2).grid(column = 1, row = 4)
        ttk.Label(rim, text = 'hours').grid(column = 2, row = 4)
        ttk.Button(rim, text = '<<', width = min, 
                                command = self.__hours_left)\
                   .grid(column = 0, row = 4, padx = x, pady = y)
        ttk.Button(rim, text = '>>', width = min,
                                command = self.__hours_right)\
                    .grid(column = 4, row = 4, padx = x, pady = y)
        ttk.Label(rim, textvariable = boss.minutes, 
                        width = 2).grid(column = 1, row = 5)
        ttk.Button(rim, text = '<<', width = min,
                command = self.__minutes_left).grid(column = 0, row = 5)

        ttk.Button(rim, text = '>>', width = min,
                command = self.__minutes_right).grid(column = 4, row = 5)
        ttk.Label(rim, text = 'minutes').grid(column = 2, 
                            row = 5)

        
    def __hours_left(self) -> None:
        if self.__boss.hours.get() == 0:
            self.__boss.hours.set(23)
        else:
            self.__boss.hours.set(self.__boss.hours.get() - 1)

    def __hours_right(self) -> None:
        if self.__boss.hours.get() == 23:
            self.__boss.hours.set(0)
        else:
            self.__boss.hours.set(self.__boss.hours.get() + 1)

    def __minutes_left(self) -> None:
        if self.__boss.minutes.get() == 0:
            self.__boss.minutes.set(59)
        else:
            self.__boss.minutes.set(self.__boss.minutes.get() - 1)
    
    def __minutes_right(self) -> None:
        if self.__boss.minutes.get() == 59:
            self.__boss.minutes.set(0)
        else:
            self.__boss.minutes.set(self.__boss.minutes.get() + 1)
