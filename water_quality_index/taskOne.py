import tkinter as tk

from selectPage import SelectPage
from vars import Vars


class TaskOne(SelectPage):

    def __init__(self, parent, controller):
        self.pH = "pH"
        self.temp = "Tempurature"
        self.wind = "Turbidity"
        self.tdv = "Total Dissolved Values"
        self.ns = "Nitrates"
        self.fc = "Fecal Coliform"
        
        self.words = [self.pH, self.wind, self.temp, self.tdv, self.ns, self.fc]

        self.weights = {
            self.pH: 0.11,
            self.temp: 0.10,
            self.wind: 0.08,
            self.tdv: 0.07,
            self.ns: 0.10,
            self.fc: 0.16
        }
        
        self.textFields = {}
        self.labelFields = {}

        self.cal_value = tk.StringVar()
        self.cal_value.set("Not Calculated")

        SelectPage.__init__(self, parent, controller)
        # self.initUI(parent, controller)

    # def initUI(self, parent, controller):

        for idx, i in enumerate(self.words):
            self.labelFields[i] = tk.Label(self, text = i, font = Vars.LABEL_FONT)
            self.textFields[i] = tk.Entry(self, validate='key', 
                                                vcmd=(controller.register(self.validate_float), '%P'))
            self.labelFields[i].place(x = 200, y = 50 + (50 * idx))
            self.textFields[i].place(x = 450, y = 50 + (50 * idx))

        self.calculate = tk.Button(self, text = "Calculate", 
        command =  lambda: self._calculate_wqi(), 
        padx = 10,
        pady = 10)
        self.calculate.place(x = 350, y = 350, width = 125, height = 35)

        self.curr_value = tk.Label(self, textvariable = self.cal_value, font = Vars.LABEL_FONT)
        self.curr_value.place(x = 500, y = 350)

    def validate_float(self, inp, empty = 0):
        try:
            if inp != "" or empty:
                float(inp)
        except:
            return False
        return True


    def _calculate_wqi(self):
        validate = True
        for i in self.words:
            validate = validate and self.validate_float(self.textFields[i].get(), 1)
        
        sum = 0
        if validate:
            for i in self.words:
                sum += (self.weights[i] * float(self.textFields[i].get()))
            self.cal_value.set(sum)
        else:
            self.cal_value.set("Enter all Inputs")
