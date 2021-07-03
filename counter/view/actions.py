import tkinter as tk
import tkinter.ttk as ttk

class Actions:
    def __init__(self, boss: tk.Tk, rim: ttk.LabelFrame) -> None:
        self.__rim = rim
        self.__new_button = ttk.Button(self.__rim, text ='new',
                                    command = boss.destroy)
        self.__new_button.grid(column = 0, row = 0)
        
    def instance(self) -> ttk.LabelFrame:
        return self.__rim