import tkinter as tk

from selectPage import SelectPage
from vars import Vars


class TaskThree(SelectPage):

    def __init__(self, parent, controller):
        SelectPage.__init__(self, parent, controller)
        label = tk.Label(self, text = "Task Three", font = Vars.LARGE_FONT)
        label.place(x = 450, y = 300)
        # label.grid(pady = 10, padx = 10, row = 5, column = 0)
