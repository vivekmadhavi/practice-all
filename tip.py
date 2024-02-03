from tkinter import *
from tkinter.messagebox import *
import re

root = Tk()
root.geometry("1200x900+100+100")
f = ("Arial", 40, "bold")
fs = ("Arial", 25, "bold")

class TipCalculator():
    def __init__(self):
        self.m_cost = StringVar()
        self.t_p = IntVar()
        self.tip = StringVar()
        self.total_cost = StringVar()

    @staticmethod
    def validate_input(input):
        if input.isspace() or any(char.isalpha() for char in input):
            raise ValueError("Number cannot be space or alphabet")

        if not re.match(r'^-?\d+([.,]\d+)?$', input):
            raise ValueError("Number cannot contain special characters")
        if not input:
            raise ValueError("Number cannot be blank")

    def validate_inputtip(self, inputtip):
        if inputtip.isspace() or any(char.isalpha() for char in inputtip):
            raise ValueError("Number cannot be space or alphabet")
        

    def gt(self, input, inputtip):
        try:
            self.validate_input(input)
            self.validate_inputtip(inputtip)
            per = self.t_p.get() / 100
            billamt = int(self.m_cost.get())
            tipentry_var = billamt * per
            self.tip.set(tipentry_var)
            final_bill = billamt + tipentry_var
            self.total_cost.set(final_bill)
        except ValueError as ve:
            showerror("Input Error", ve)
        except Exception as e:
            showerror("Issue", e)

    def button(self):
        input_value = billEntry.get().strip()
        input_tip = tipentry.get().strip()
        self.gt(input_value, input_tip)

tip_calculator = TipCalculator()

tlabel = Label(root, text="Tip Calculator", font=f)
billlabel = Label(root, text="Enter Bill Amount:-", font=fs)
billEntry = Entry(root, textvariable=tip_calculator.m_cost, font=fs)
tippercent = Label(root, text="Tip percentage:-", font=fs)
tipfive = Radiobutton(root, text="5%", font=fs, variable=tip_calculator.t_p, value=5)
tipten = Radiobutton(root, text="10%", font=fs, variable=tip_calculator.t_p, value=10)
tipfifteen = Radiobutton(root, text="15%", font=fs, variable=tip_calculator.t_p, value=15)
tiptwenty = Radiobutton(root, text="20%", font=fs, variable=tip_calculator.t_p, value=20)
tiptwentyfive = Radiobutton(root, text="25%", font=fs, variable=tip_calculator.t_p, value=25)
tipthirty = Radiobutton(root, text="30%", font=fs, variable=tip_calculator.t_p, value=30)
tiplabel = Label(root, text="Tip Amount:-", font=fs)
tipentry = Entry(root, textvariable=tip_calculator.tip, font=fs)
total = Label(root, text="Total Bill :-", font=fs)
totalbill = Entry(root, textvariable=tip_calculator.total_cost, font=fs)
btn = Button(root, text="Find", font=f, command=tip_calculator.button)

tlabel.place(x=420, y=10)
billlabel.place(x=20, y=100)
billEntry.place(x=400, y=100)
tippercent.place(x=20, y=250)
tipfive.place(x=400, y=250)
tipten.place(x=500, y=250)
tipfifteen.place(x=600, y=250)
tiptwenty.place(x=700, y=250)
tiptwentyfive.place(x=800, y=250)
tipthirty.place(x=900, y=250)
tiplabel.place(x=20, y=400)
total.place(x=20, y=550)
totalbill.place(x=400, y=550)
tipentry.place(x=400, y=400)
btn.place(x=550, y=700)

root.mainloop()