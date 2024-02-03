import re
from tkinter import *
from tkinter import messagebox

def validate_input(mb_input):
    if ' ' in mb_input:
        raise ValueError("MB amount cannot contain spaces")
    if mb_input.isalpha():
        raise ValueError("MB amount should not contain alphabets")
    if not re.match("^-?\d+(\.\d+)?$", mb_input):
        raise ValueError("MB amount cannot contain special characters")
    if not mb_input:
        raise ValueError("MB amount cannot be blank")
   
    min_limit = 0
    max_limit = 100000000
    mb = float(mb_input)
    if not (min_limit <= mb <= max_limit):
        raise ValueError(f"MB amount must be between {min_limit} and {max_limit}")

def convert(mb_input):
    try:
        validate_input(mb_input)
        mb = float(mb_input)
        tb = mb / (1024 ** 2)
        return tb
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def button():
    try:
        mb_input = mb_entry.get().strip()
        result_label.config(text="")
        tb_result = convert(mb_input)
        result_label.config(text=f"{mb_input} megabytes is equal to {tb_result:.6f} terabytes")
        mb_entry.focus()
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

root = Tk()
root.title("Megabyte to Terabyte Converter")
root.geometry("1400x700+50+50")
f = ("Century", 30, "bold", "italic")

labTitle = Label(root, text="MB to TB Converter", font=f)
labTitle.place(x=300, y=50)

mb_label = Label(root, text="Enter MB: ", font=f)
mb_entry = Entry(root, font=f)
convert_button = Button(root, command=button, font=f, text="Convert")
result_label = Label(root, font=f)

mb_label.place(x=50, y=150)
mb_entry.place(x=400, y=150)
convert_button.place(x=400, y=250)
result_label.place(x=100, y=400)

# Set the focus on the entry widget when the application starts
mb_entry.focus()

root.mainloop()
