import tkinter as tk

from selectPage import SelectPage
from vars import Vars

class HomePage(SelectPage):

    def __init__(self, parent, controller):
        SelectPage.__init__(self, parent, controller)
        label = tk.Label(self, text = "Home", font = Vars.LARGE_FONT)
        label.place(x = 450, y = 300)
        instruct = tk.Label(self, text = "In this page we have instructions", font = Vars.LABEL_FONT)
        instruct.place(x = 450, y = 400)
