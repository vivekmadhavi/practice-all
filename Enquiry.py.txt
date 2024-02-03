from tkinter import *
from sqlite3 import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *

def create_table():
    con = None
    try:
        con = connect("cc.db")
        print("Connected to the database")
        cursor = con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS student (
                            name TEXT,
                            phone INTEGER,
                            address TEXT,
                            lang TEXT,
                            query TEXT
                        )''')
        con.commit()
        print("Table created successfully")
    except Exception as e:
        con.rollback()
        print(f"An error occurred while creating the table: {e}")
    finally:
        if con is not None:
            con.close()

def delete_selected_data():
    con = None
    try:
        create_table()
        con = connect("cc.db")
        cursor = con.cursor()
        selected_data = dtview.get("sel.first", "sel.last")
        if not selected_data:
            showwarning("Warning", "No data selected to delete.")
            return

        name = selected_data.split('\n')[0].split(': ')[1]
        cursor.execute("DELETE FROM student WHERE name=?", (name,))
        con.commit()

        showinfo("Success", "Selected data deleted successfully.")
        # Refresh the view after deletion
        f7()
    except Exception as e:
        showerror("Issue", f"An error occurred during data deletion: {e}")
    finally:
        if con is not None:
            con.close()

def f1():
    addstu.deiconify()
    root.withdraw()

def f2():
    root.deiconify()
    addstu.withdraw()

def f4():
    root.deiconify()
    manage.withdraw()

def f3():
    manage.deiconify()
    root.withdraw()

def f6():
    manage.deiconify()
    dt.withdraw()

def f7():
    for widget in dt.winfo_children():
        widget.destroy()

    con = None
    try:
        con = connect("cc.db")
        cursor = con.cursor()
        sql = "SELECT rowid, * FROM student"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            container = Frame(dt, pady=5)
            container.pack(fill=X)

            info = f"Name: {d[1]}, Phone: {d[2]}, Address: {d[3]}, Lang: {d[4]}, Query: {d[5]}"
            label = Label(container, text=info, font=f, wraplength=800, justify=LEFT)
            label.pack(side=LEFT, padx=10)

            delete_btn = Button(container, text="Delete", command=lambda id=d[0], cont=container: delete_record(id, cont))
            delete_btn.pack(side=RIGHT, padx=10)
    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

    back_btn = Button(dt, text="Back", font=f, command=f6)
    back_btn.pack(pady=10)

def f5():
    try:
        if mentry.get() == "admin" and mpassword.get() == "admin":
            dt.deiconify()
            manage.withdraw()
            f7()
        else:
            showerror("Invalid", "Invalid username or password")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_record(record_id, container):
    con = None
    try:
        con = connect("cc.db")
        cursor = con.cursor()
        sql = "DELETE FROM student WHERE rowid = ?"
        cursor.execute(sql, (record_id,))
        con.commit()
        showinfo("Success", "Record deleted")
        container.destroy()
    except Exception as e:
        showerror("Issue", f"An error occurred during data deletion: {e}")
    finally:
        if con is not None:
            con.close()
def validation_input():
    if not nameentry.get().replace(" ", "").isalpha():
        showerror("Error", "Invalid name")
    elif not phoneentry.get().isdigit():
        showerror("Error", "Invalid phone number")
    else:
        save()

def save():
    global a, b, c, d, e
    con = None
    try:
        create_table()
        con = connect("cc.db")
        print("Connected to the database for data insertion")
        cursor = con.cursor()
        sql = "INSERT INTO student VALUES (?, ?, ?, ?, ?)"
        name = nameentry.get()
        phone = int(phoneentry.get())
        address = addressentry.get()
        lang = ""
        if a.get():
            lang += "product1"
        if b.get():
            lang += "product2"
        if c.get():
            lang += "product3"
        if d.get():
            lang += "product4"
        if e.get():
            lang += "product5"
        query = queryentry.get()
        cursor.execute(sql, (name, phone, address, lang, query))
        con.commit()
        showinfo("Success", "Record created")
        nameentry.delete(0, END)
        phoneentry.delete(0, END)
        addressentry.delete(0, END)
        queryentry.delete(0, END)
        nameentry.focus()

        # Call f7 after saving the record to refresh the view
        f7()
    except Exception as e:
        con.rollback()
        showerror("Issue", f"An error occurred during data insertion: {e}")
    finally:
        if con is not None:
            con.close()

button_style = {
    'font': ('Arial', 30),
    'bg': '#4CAF50',  # Green background color
    'fg': 'white',    # White text color
    'activebackground': '#45a049',  # Darker green on hover
    'bd': 0,  # No border
    'padx': 10,  # Horizontal padding
    'pady': 5,   # Vertical padding
}

button_style1 = {
    'font': ('Arial', 30),
    'bg': 'black',  # Green background color
    'fg': 'white',    # White text color
    'activebackground': 'white',  # Darker green on hover
    'bd': 0,  # No border
    'padx': 10,  # Horizontal padding
    'pady': 5,   # Vertical padding
}

root = Tk()
root.title("Enquiry")
root.geometry("900x900+50+50")
f = ("Arial",30,"bold")
fa = ("Arial",40,"bold")
y = 10

btnAdd = Button(root, text="User", width=13, command=f1,**button_style)
btnView = Button(root, text="Manager", width=13, command=f3,**button_style)
btnAdd.pack(pady=y)
btnView.pack(pady=y)

a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()
e = IntVar()
addstu = Toplevel(root)
addstu.title("Add student")
addstu.geometry("900x900+50+50")
addlabel = Label(addstu, text="Enquiry", font=fa)
addname = Label(addstu, text="Name:", font=f)
nameentry = Entry(addstu, font=f)
addphone = Label(addstu, text="Phone:", font=f)
phoneentry = Entry(addstu, font=f)
addaddress = Label(addstu, text="Address:", font=f)
addressentry = Entry(addstu, font=f)
addquery = Label(addstu, text="Query:", font=f)
labselect = Label(addstu, text="Select : ", font=f)
entproduct1 = Checkbutton(addstu, font=f, text="pd1", variable=a)
entproduct2 = Checkbutton(addstu, font=f, text="pd2", variable=b)
entproduct3 = Checkbutton(addstu, font=f, text="pd3", variable=c)
entproduct4 = Checkbutton(addstu, font=f, text="pd4", variable=d)
entproduct5 = Checkbutton(addstu, font=f, text="pd5", variable=e)
queryentry = Entry(addstu, font=f)
bkbtn = Button(addstu, text="back", font=f, command=f2)
addlabel.place(x=370, y=10)
addname.place(x=20, y=100)
nameentry.place(x=300, y=100)
addphone.place(x=20, y=200)
phoneentry.place(x=300, y=200)
addaddress.place(x=20, y=300)
addressentry.place(x=300, y=300)
labselect.place(x=20, y=400)
entproduct1.place(x=300, y=400)
entproduct2.place(x=420, y=400)
entproduct3.place(x=540, y=400)
entproduct4.place(x=660, y=400)
entproduct5.place(x=780, y=400)
addquery.place(x=20, y=500)
queryentry.place(x=300, y=500)
subbtn = Button(addstu, text="send", command=validation_input,**button_style)
subbtn.place(x=400, y=600)
bkbtn.place(x=400, y=700)
addstu.configure(bg='lightgray')
addstu.withdraw()

manage = Toplevel(root)
manage.title("Manager login")
manage.geometry("900x900+50+50")

mlabel = Label(manage, text="Manager Login", font=fa)
mentry = Entry(manage, font=f)
mpassword = Entry(manage, show="*", font=f)
mlbtn = Button(manage, text="Login", font=f, command=f5)
mlabel.pack(pady=y)
mentry.pack(pady=y)
mpassword.pack(pady=y)
mlbtn.pack(pady=y)
mbtn = Button(manage, text="back", font=f, command=f4)
mbtn.pack(pady=y)
manage.configure(bg='lightgray')
manage.withdraw()

dt = Toplevel(root)
dt.title("Manager login")
dt.geometry("900x900+50+50")
dtlistbox = Listbox(dt, width=80, height=20, font=f)
dtlistbox.pack(pady=y)
bk = Button(dt, text="back", command=f6,**button_style1)
bk.pack(pady=y)
dt.withdraw()

root.configure(bg='lightgray')
root.mainloop()