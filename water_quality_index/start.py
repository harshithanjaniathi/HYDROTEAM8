import tkinter as tk

from homePage import HomePage
from taskOne import TaskOne
from taskTwo import TaskTwo
from taskThree import TaskThree



LARGE_FONT = ("Verdana", 40)
LABEL_FONT = ("Verdana", 15)

class HydroApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)
        self.wm_title("Water Quality Index Estimation Tool")
        self.geometry("900x600")

        container = tk.Frame(self)

        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for Frame in (HomePage, TaskOne, TaskTwo, TaskThree):            
            frame = Frame(container, self)
            self.frames[Frame] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(HomePage)    


    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
    

# class SelectPage(tk.Frame):

#     def __init__(self, parent, controller):

#         tk.Frame.__init__(self, parent)
#         self.configure(background = '#D6E9D2')
#         self.initUI(parent, controller)

#     def initUI(self, parent, controller):

#         HomeButton = self.custom_button(text = "Home", 
#         command =  lambda: controller.show_frame(HomePage))
#         HomeButton.place(x = 10, y = 10, width = 125, height = 35)

#         TaskOneButton = self.custom_button(text = "TaskOne", 
#         command =  lambda: controller.show_frame(TaskOne))
#         TaskOneButton.place(x = 10, y = 50, width = 125, height = 35)

#         TaskTwoButton = self.custom_button(text = "TaskTwo", 
#         command =  lambda: controller.show_frame(TaskTwo))
#         TaskTwoButton.place(x = 10, y = 90, width = 125, height = 35)

#         TaskThreeButton = self.custom_button(text = "TaskThree", 
#         command =  lambda: controller.show_frame(TaskThree))
#         TaskThreeButton.place(x = 10, y = 130, width = 125, height = 35)

#     def custom_button(self, text, command):
#         return tk.Button(self, text = text, 
#         command =  command, 
#         padx = 10,
#         pady = 10)

#     def nextPage(self):
#         print("DONE")

# class HomePage(SelectPage):

#     def __init__(self, parent, controller):
#         SelectPage.__init__(self, parent, controller)
#         label = tk.Label(self, text = "Home", font = LARGE_FONT)
#         label.place(x = 450, y = 300)
#         instruct = tk.Label(self, text = "In this page we have instructions", font = LABEL_FONT)
#         instruct.place(x = 450, y = 400)


# class TaskOne(SelectPage):

#     def __init__(self, parent, controller):
#         self.pH = "pH"
#         self.temp = "Tempurature"
#         self.wind = "Turbidity"
#         self.tdv = "Total Dissolved Values"
#         self.ns = "Nitrates"
#         self.fc = "Fecal Coliform"
        
#         self.words = [self.pH, self.wind, self.temp, self.tdv, self.ns, self.fc]

#         self.weights = {
#             self.pH: 0.11,
#             self.temp: 0.10,
#             self.wind: 0.08,
#             self.tdv: 0.07,
#             self.ns: 0.10,
#             self.fc: 0.16
#         }
        
#         self.textFields = {}
#         self.labelFields = {}

#         self.cal_value = tk.StringVar()
#         self.cal_value.set("Not Calculated")

#         SelectPage.__init__(self, parent, controller)
#         # self.initUI(parent, controller)

#     # def initUI(self, parent, controller):

#         for idx, i in enumerate(self.words):
#             self.labelFields[i] = tk.Label(self, text = i, font = LABEL_FONT)
#             self.textFields[i] = tk.Entry(self, validate='key', 
#                                                 vcmd=(controller.register(self.validate_float), '%P'))
#             self.labelFields[i].place(x = 50, y = 200 + (50 * idx))
#             self.textFields[i].place(x = 50, y = 225 + (50 * idx))

#         self.calculate = tk.Button(self, text = "Calculate", 
#         command =  lambda: self._calculate_wqi(), 
#         padx = 10,
#         pady = 10)
#         self.calculate.place(x = 50, y = 550, width = 125, height = 35)

#         self.curr_value = tk.Label(self, textvariable = self.cal_value, font = LABEL_FONT)
#         self.curr_value.place(x = 400, y = 250)

#     def validate_float(self, inp, empty = 0):
#         try:
#             if inp != "" or empty:
#                 float(inp)
#         except:
#             return False
#         return True


#     def _calculate_wqi(self):
#         validate = True
#         for i in self.words:
#             validate = validate and self.validate_float(self.textFields[i].get(), 1)
        
#         sum = 0
#         if validate:
#             for i in self.words:
#                 sum += (self.weights[i] * float(self.textFields[i].get()))
#             self.cal_value.set(sum)
#         else:
#             self.cal_value.set("Enter all Inputs")


# class TaskTwo(SelectPage):

#     def __init__(self, parent, controller):
#         SelectPage.__init__(self, parent, controller)
#         label = tk.Label(self, text = "Task Two", font = LARGE_FONT)
#         label.place(x = 450, y = 300)
#         # label.grid(pady = 10, padx = 10, row = 5, column = 0)

# class TaskThree(SelectPage):

#     def __init__(self, parent, controller):
#         SelectPage.__init__(self, parent, controller)
#         label = tk.Label(self, text = "Task Three", font = LARGE_FONT)
#         label.place(x = 450, y = 300)
#         # label.grid(pady = 10, padx = 10, row = 5, column = 0)


app = HydroApp()
app.mainloop()
