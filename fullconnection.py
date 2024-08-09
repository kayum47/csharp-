import mysql.connector # type: ignore
from tkinter import *
from tkinter import messagebox

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="kp"
)

mycursor = mydb.cursor()

def searchid():
  id = txtid.get()
  sql = "select * from stud where id = %s"
  values = (id ,)
  mycursor.execute(sql,values)
  myresult = mycursor.fetchall()
  count = len(myresult)
  if count >=1 :
    for x in myresult:
      txtname.delete(0,END)
      txtclass.delete(0,END)
      txtname.insert(1,x[1])
      txtclass.insert(1,x[2])
  else:
    messagebox.showinfo("Error","No record found")
root = Tk()
Label(root,text="Enter ID to search",font ="Ubuntu").pack(pady="2")
txtid = Entry(root,font="Ubuntu")
txtid.pack(pady ="2")
Button(root ,text="Sreach Record",command=searchid).pack()
txtname = Entry(root ,font ="Ubuntu")
txtname.pack(pady="2")
txtclass = Entry(root ,font ="Ubuntu")
txtclass.pack(pady="2")
root.mainloop()
