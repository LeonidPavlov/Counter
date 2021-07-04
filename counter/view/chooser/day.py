import tkinter as tk
import tkinter.ttk as ttk
from datetime import datetime as dt

from counter.view.chooser.month import Month
from counter.model.event_time import Event_Time

day_name = ['monday', 'tuesday', 'wednesday', 'thursday',
                    'friday', 'saturday', 'sunday']

class Day:

    def __init__(self, boss: tk.Tk, rim: ttk.LabelFrame, 
                                            month: Month) -> None:
        self.__boss: tk.Tk = boss
        self.__rim: ttk.LabelFrame = rim
        self.__month: Month = month

        ttk.Button(self.__rim, text = '<<', width = min,
                            command = self.__rewind_left)\
                                .grid(column = 0, row = 2, pady = 3)
        ttk.Label(self.__rim, textvariable = self.__boss.day)\
                                .grid(column = 1, row = 2)
        ttk.Label(self.__rim, textvariable = self.__boss.day_name, width = 10)\
                                .grid(column = 2, row = 2, columnspan = 2)
        ttk.Button(self.__rim, text = '>>', width = min,
                                command = self.__rewind_right)\
                                .grid(column = 4, row = 2)
        self.__define_day_name()

    def __rewind_left(self) -> None:
        if self.__boss.day.get() > 1:
            self.__boss.day.set(self.__boss.day.get() - 1)
        if self.__boss.day.get() == 1:
            self.__month.rewind_left()
            self.__boss.day.set(self.__define_amount_days())
        self.__define_day_name()
                                                                            
    def __rewind_right(self) -> None:
        amount_days: int = self.__define_amount_days()
        if self.__boss.day.get() < amount_days:
            self.__boss.day.set(self.__boss.day.get() + 1)
        else:
            self.__boss.day.set(1)
            self.__month.rewind_right()
        self.__define_day_name()

    def __define_day_name(self) -> None:
        date = dt(self.__boss.year.get(), self.__boss.month.get(),
                                            self.__boss.day.get())
        self.__boss.day_name.set(day_name[date.weekday()])    

    def __define_amount_days(self) -> int:
        ammount_days = {1: 31, 2: 0, 3: 31, 4: 30, 
                        5: 31, 6: 30, 7: 31, 8: 31,
                        9: 30, 10: 31, 11: 30, 12: 31}
        if Event_Time.is_leap(self.__boss.year.get()):
            ammount_days[2] = 29
        else:
            ammount_days[2] = 28
        return ammount_days[self.__boss.month.get()]  
    
    def on_change_year_do_something(self) -> None:
        self.__define_day_name()

    def on_change_month_do_something(self) -> None:
        amount: int = self.__define_amount_days()
        if self.__boss.day.get() > amount:
            self.__boss.day.set(amount)
        self.__define_day_name()