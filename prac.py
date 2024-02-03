from tkinter import *
from sqlite3 import *
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
        selected_index = dtlistbox.curselection()
        if not selected_index:
            showwarning("Warning", "No data selected to delete.")
            return

        name = dtlistbox.get(selected_index).split(':')[1].strip()
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
    dtlistbox.delete(0, END)

    con = None
    try:
        con = connect("cc.db")
        cursor = con.cursor()
        sql = "SELECT rowid, * FROM student"
        cursor.execute(sql)
        data = cursor.fetchall()
        for d in data:
            info = f"Name: {d[1]}, Phone: {d[2]}, Address: {d[3]}, Lang: {d[4]}, Query: {d[5]}"
            dtlistbox.insert(END, info)
    except Exception as e:
        showerror("Issue", e)
    finally:
        if con is not None:
            con.close()

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

root = Tk()
root.title("S.M .S by kamal sir")
root.geometry("900x700+50+50")
f = ("Arial", 14, "bold")
fa = ("Arial", 16, "bold")
y = 10

btnAdd = Button(root, text="User", font=f, width=13, command=f1)
btnView = Button(root, text="Manager", font=f, width=13, command=f3)
btnAdd.pack(pady=y)
btnView.pack(pady=y)

a = IntVar()
b = IntVar()
c = IntVar()
d = IntVar()
e = IntVar()
addstu = Toplevel(root)
addstu.title("Add student")
addstu.geometry("600x500+50+50")
addlabel = Label(addstu, text="Enquiry", font=fa)
addname = Label(addstu, text="Name:", font=f)
nameentry = Entry(addstu, font=f)
addphone = Label(addstu, text="Phone:", font=f)
phoneentry = Entry(addstu, font=f)
addaddress = Label(addstu, text="Address:", font=f)
addressentry = Entry(addstu, font=f)
addquery = Label(addstu, text="Query:", font=f)
labselect = Label(addstu, text="Select Products:", font=f)
entproduct1 = Checkbutton(addstu, font=f, text="Product1", variable=a)
entproduct2 = Checkbutton(addstu, font=f, text="Product2", variable=b)
entproduct3 = Checkbutton(addstu, font=f, text="Product3", variable=c)
entproduct4 = Checkbutton(addstu, font=f, text="Product4", variable=d)
entproduct5 = Checkbutton(addstu, font=f, text="Product5", variable=e)
queryentry = Entry(addstu, font=f)
subbtn = Button(addstu, text="Send", font=f, command=save)
bkbtn = Button(addstu, text="Back", font=f, command=f2)
addlabel.pack(pady=10)
addname.pack(pady=5)
nameentry.pack(pady=5)
addphone.pack(pady=5)
phoneentry.pack(pady=5)
addaddress.pack(pady=5)
addressentry.pack(pady=5)
labselect.pack(pady=5)
entproduct1.pack(pady=5)
entproduct2.pack(pady=5)
entproduct3.pack(pady=5)
entproduct4.pack(pady=5)
entproduct5.pack(pady=5)
addquery.pack(pady=5)
queryentry.pack(pady=5)
subbtn.pack(pady=10)
bkbtn.pack(pady=10)
addstu.withdraw()

manage = Toplevel(root)
manage.title("Manager login")
manage.geometry("600x300+50+50")
mlabel = Label(manage, text="Manager Login", font=fa)
mentry = Entry(manage, font=f)
mpassword = Entry(manage, show="*", font=f)
mlbtn = Button(manage, text="Login", font=f, command=f5)
mlabel.pack(pady=10)
mentry.pack(pady=10)
mpassword.pack(pady=10)
mlbtn.pack(pady=10)
mbtn = Button(manage, text="Back", font=f, command=f4)
mbtn.pack(pady=10)
manage.withdraw()

dt = Toplevel(root)
dt.title("Data Display")
dt.geometry("900x600+50+50")
dtlistbox = Listbox(dt, width=80, height=20, font=f, selectmode=SINGLE)
dtlistbox.pack(pady=10)
delete_btn = Button(dt, text="Delete Selected Data", font=f, command=delete_selected_data)
delete_btn.pack(pady=10)
bk = Button(dt, text="Back", font=f, command=f6)
bk.pack(pady=10)
dt.withdraw()

root.mainloop()