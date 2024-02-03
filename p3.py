from tkinter import *
from sqlite3 import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *

def f1():
	addstu.deiconify()
	root.withdraw()

def f2():
	root.deiconify()
	addstu.withdraw()

def f3():
	viewstu.deiconify()
	root.withdraw()
	vs_stdata.delete(1.0,END)
	con = None
	try:
		con = connect("kc.db")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "rno" + str(d[0]) + "name" + str(d[1]) + "\n"
		vs_stdata.insert(INSERT, info)
	except Exception as e:
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

def f4():
	root.deiconify()
	viewstu.withdraw()

def save():
	con = None
	try:
		con = connect("kc.db")
		cursor=con.cursor()
		sql="insert into student values('%d','%s')"
		rno = int(as_entroll.get())
		name = as_entname.get()
		cursor.execute(sql % (rno , name))
		con.commit()
		showinfo("success","record created")
		as_entroll.delete(0,END)
		as_entname.delete(0,END)
		as_entroll.focus()
	except Exception as e:
		con.rollback()
		showerror("issue",e)
	finally:
		if con is not None:
			con.close()

	
root = Tk()
root.title("S.M .S by kamal sir")
root.geometry("500x600+50+50")
f = ("Arial",30,"bold")
y=10


btnAdd=Button(root,text="add",font=f,width=13,command=f1)
btnView=Button(root,text="View",font=f,width=13,command=f3)
btnAdd.pack(pady=y)
btnView.pack(pady=y)


addstu=Toplevel(root)
addstu.title("Add student")
addstu.geometry("500x600")

as_labroll=Label(addstu,text="enter roll no",font=f)
as_entroll=Entry(addstu,font=f)
as_labname=Label(addstu,text="enter name",font=f)
as_entname=Entry(addstu,font=f)
as_btnsave=Button(addstu,text="save",font=f,command=save)
as_btnback=Button(addstu,text="back to main",font=f,command=f2)


as_labroll.pack(pady=y)
as_entroll.pack(pady=y)
as_labname.pack(pady=y)
as_entname.pack(pady=y)
as_btnsave.pack(pady=y)
as_btnback.pack(pady=y)
addstu.withdraw()



viewstu=Toplevel(root)
viewstu.title="view student"
viewstu.geometry("500x600")
vs_stdata= ScrolledText(viewstu,width=20,height=10,font=f)
vs_btnback=Button(viewstu,text="Back yo main",font=f,command=f4)
vs_stdata.pack(pady=y)
vs_btnback.pack(pady=y)
viewstu.withdraw()










root.mainloop()
